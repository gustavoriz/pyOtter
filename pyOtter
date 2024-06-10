class pyOtter:
    def __init__(self, data=None, columns=None):
        self.data = data if data is not None else []
        self.columns = columns if columns is not None else []

    @classmethod
    def from_spark_dataframe(cls, spark_df):
        columns = spark_df.columns
        data = [row.asDict() for row in spark_df.collect()]
        return cls(data, columns)

    def filter(self, condition):
        filtered_data = [row for row in self.data if condition(row)]
        return MeuDataFrame(filtered_data, self.columns)

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
        return MeuDataFrame(joined_data, joined_columns)

    def __str__(self):
        header = "\t".join(self.columns)
        rows = "\n".join("\t".join(str(row[col]) for col in self.columns) for row in self.data)
        return f"{header}\n{rows}"
