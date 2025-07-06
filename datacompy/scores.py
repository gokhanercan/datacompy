from msilib.schema import SelfReg


class Scores(object):

    def __init__(self, **kwargs):
        super().__init__()
        self.target_cells = None
        self.source_cells = None
        self.cols_in_common = None
        self.cols_in_target = None
        self.matching_rows = None
        self.rows_in_target = None
        self.matching_cols = None
        self.matching_cells = None
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def column_schema_similarity(self) -> float:       #todo: take into account data types too.
        return self.cols_in_common / max(self.cols_in_target, self.cols_in_common) if self.cols_in_target else 0

    @property
    def overall_schema_similarity(self) -> float:
        return self.column_schema_similarity

    def overall_data_similarity(self) -> float:
        return self.row_similarity #TODO: Not working cell by cell comparison yet, so using row similarity for now.

    @property
    def row_similarity(self) -> float:
        if(self.overall_schema_similarity == 1):
            return self.matching_rows / max(self.rows_in_target, self.matching_rows) if self.rows_in_target else 0
        else:
            return None # todo:

    @property
    def column_similarity(self) -> float:
        if (self.overall_schema_similarity == 1):
            return self.matching_cols / max(self.cols_in_target, self.matching_cols) if self.cols_in_target else 0
        else:
            return None  # todo:

    @property
    def cell_similarity(self) -> float:
        return self.matching_cells / max(self.target_cells, self.matching_cells) if self.target_cells else 0

    def __str__(self):
        base_attrs = self.__dict__
        prop_attrs = {
            'column_schema_similarity': self.column_schema_similarity,
            'overall_schema_similarity': self.overall_schema_similarity,
            'row_similarity': self.row_similarity,
            'column_similarity': self.column_similarity,
            'cell_similarity': self.cell_similarity
        }
        all_attrs = {**base_attrs, **prop_attrs}
        return '\n'.join(f"{k}: {v}" for k, v in all_attrs.items())