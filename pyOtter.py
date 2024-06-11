# This library was created to convert spark dataframes or pandas dataframes to otter dataframes
# Created by: Gustavo Riz
# Version: 1.1
class pyOtter:
    def __init__(self, data=None, columns=None):
        self.data = data if data is not None else []
        self.columns = columns if columns is not None else []

    @classmethod
    def from_spark_dataframe(cls, spark_df):
        columns = spark_df.columns
        data = [row.asDict() for row in spark_df.collect()]
        return cls(data, columns)

    def from_big_spark_dataframe(cls, spark_df):
        def process_partition(iterator):
            return [row.asDict() for row in iterator]

        data = spark_df.rdd.mapPartitions(process_partition).reduce(lambda x, y: x + y)
        columns = spark_df.columns
        return cls(data, columns)

    def from_pandas_dataframe(cls, pandas_df):
        columns = pandas_df.columns.tolist()
        data = pandas_df.to_dict(orient='records')
        return cls(data, columns)

    def to_pandas_dataframe(self):
        return pd.DataFrame(self.data, columns=self.columns)

    def to_spark_dataframe(self, spark_session):
        return spark_session.createDataFrame(self.data)
    
    def count_rows(self):
        return len(self.data)

    def rename_columns(self, col_rename_map):
        self.columns = [col_rename_map.get(col, col) for col in self.columns]
        for row in self.data:
            for old_col, new_col in col_rename_map.items():
                if old_col in row:
                    row[new_col] = row.pop(old_col)
    
    def show_schema(self):
        return {col: type(next(iter(self.data))[col]) for col in self.columns} if self.data else {}

    def change_schema(self, col_type_map):
        for row in self.data:
            for col, new_type in col_type_map.items():
                if col in row:
                    row[col] = new_type(row[col])

    def filter(self, **conditions):
        filtered_data = []
        for row in self.data:
            include_row = True
            for col, value in conditions.items():
                if row.get(col) != value:
                    include_row = False
                    break
            if include_row:
                filtered_data.append(row)
        return pyOtter(filtered_data, self.columns)

    def count_distinct(self, *cols):
        distinct_values = {col: set() for col in cols}
        for row in self.data:
            for col in cols:
                distinct_values[col].add(row[col])
        return {col: len(distinct_values[col]) for col in cols}

    def export_to_csv(self, filename, delimiter=','):
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.columns, delimiter=delimiter)
            writer.writeheader()
            writer.writerows(self.data)

    def print_schema(self):
        schema = self.show_schema()
        for col, dtype in schema.items():
            print(f"{col}: {dtype}")

    def join(self, other, on, how='inner'):
        joined_data = []
        if how == 'inner':
            for row1 in self.data:
                for row2 in other.data:
                    if row1[on] == row2[on]:
                        joined_data.append({**row1, **row2})
        elif how == 'left':
            for row1 in self.data:
                matched = False
                for row2 in other.data:
                    if row1[on] == row2[on]:
                        joined_data.append({**row1, **row2})
                        matched = True
                if not matched:
                    joined_data.append(row1)
        elif how == 'right':
            for row2 in other.data:
                matched = False
                for row1 in self.data:
                    if row1[on] == row2[on]:
                        joined_data.append({**row1, **row2})
                        matched = True
                if not matched:
                    joined_data.append(row2)
        elif how == 'outer':
            for row1 in self.data:
                matched = False
                for row2 in other.data:
                    if row1[on] == row2[on]:
                        joined_data.append({**row1, **row2})
                        matched = True
                if not matched:
                    joined_data.append(row1)
            for row2 in other.data:
                matched = False
                for row1 in self.data:
                    if row1[on] == row2[on]:
                        matched = True
                        break
                if not matched:
                    joined_data.append(row2)
        else:
            raise ValueError(f"Unknown join type: {how}")

        # Resolve column conflicts
        joined_columns = list(set(self.columns + other.columns))
        return pyOtter(joined_data, joined_columns)

    def __str__(self):
        header = "\t".join(self.columns)
        rows = "\n".join("\t".join(str(row.get(col, '')) for col in self.columns) for row in self.data)
        return f"{header}\n{rows}"
