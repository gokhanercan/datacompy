
class Metrics(object):

    def __init__(self, **kwargs):
        super().__init__()
        self.target_cells = None
        self.source_cells = None
        self.cols_in_common = None
        self.cols_in_target = None
        self.cols_in_source = None
        self.matching_rows = None
        self.rows_in_target = None
        self.rows_in_source = None
        self.matching_cols = None
        self.matching_cells = None
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def column_schema_similarity(self) -> float:       #todo: take into account data types too.
        return self.cols_in_common / max(self.cols_in_target, self.cols_in_common) if self.cols_in_target else 0

    @property
    def redundant_schema_score(self) -> float:
        if (self.redundant_cols == 0):
            return 1
        else:
            return self.cols_in_target / self.cols_in_source if self.cols_in_source else 0

    @property
    def redundant_data_score(self):
        if (self.redundant_rows == 0):
            return 1
        else:
            return self.rows_in_target / self.rows_in_source if self.rows_in_source else 0

    @property
    def row_similarity(self) -> float:
        if(self.redundant_schema_score == 1):
            return self.matching_rows / max(self.rows_in_target, self.matching_rows) if self.rows_in_target else 0
        else:
            return self.matching_rows / max(self.rows_in_target, self.matching_rows) if self.rows_in_target else 0 #TODO: Should be use diff. calculation when redundant columns exist

    @property
    def column_similarity(self) -> float:
        if (self.redundant_schema_score == 1):
            return self.matching_cols / max(self.cols_in_target, self.matching_cols) if self.cols_in_target else 0
        else:
            return self.matching_cols / max(self.cols_in_target, self.matching_cols) if self.cols_in_target else 0 #TODO: Should be use diff. calculation when redundant columns exist

    @property
    def cell_similarity(self) -> float:
        return self.matching_cells / max(self.target_cells, self.matching_cells) if self.target_cells else 0

    @property
    def overall_similarity(self) -> float:
        """Calculate the overall similarity score based on column schema, row, and cell similarities."""
        scores = [self.column_schema_similarity, self.cell_similarity]
        return  sum(scores) / len(scores) if scores else None

    @property
    def overall_score(self) -> float:
        scores = [self.overall_similarity, self.redundant_schema_score, self.redundant_data_score]
        return sum(scores) / len(scores) if scores else None

    @property
    def redundant_cols(self) -> float:
        """Calculate the extra columns in the target dataframe."""
        return self.cols_in_source - self.cols_in_target if self.cols_in_target else 0

    @property
    def redundant_rows(self) -> float:
        return self.rows_in_source - self.rows_in_target if self.rows_in_target else 0

    def __str__(self):
        base_attrs = self.__dict__
        prop_attrs = {
            'column_schema_similarity': self.column_schema_similarity,
            'row_similarity': self.row_similarity,
            'column_similarity': self.column_similarity,
            'cell_similarity': self.cell_similarity,
            'overall_similarity': self.overall_similarity,

            'redundant_cols': self.redundant_cols,
            'redundant_rows': self.redundant_rows,
            'redundant_schema_score': self.redundant_schema_score,
            'redundant_data_score': self.redundant_data_score,

            'overall_score': self.overall_score,
        }
        all_attrs = {**base_attrs, **prop_attrs}
        return '\n'.join(f"{k}: {v}" for k, v in all_attrs.items())