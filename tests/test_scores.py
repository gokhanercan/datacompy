import unittest
from io import StringIO

import pandas as pd

import datacompy
from datacompy.scores import Scores


class TestScores(unittest.TestCase):

    def setUp(self):
        data1 = """acct_id,dollar_amt,name             ,float_fld ,date_fld
        10000001234,123.45    ,George Maharis1     ,14530.1555,2017-01-01
        10000001235,0.45      ,Michael Bluth      ,1         ,2017-01-01
        10000001236,1345      ,George Bluth       ,          ,2017-01-01
        10000001237,123456    ,Bob Loblaw         ,345.12    ,2017-01-01
        """
        self.df = pd.read_csv(StringIO(data1.strip()))

    @staticmethod
    def _calculate_scores(df_source, df_target):
        compare = datacompy.Compare(
            df_source,
            df_target,
            join_columns='acct_id',
            abs_tol=0,
            rel_tol=0,
            df1_name='Source',
            df2_name='Target',
        )
        compare.matches(ignore_extra_columns=False)
        reports, scores = compare.report()
        return scores

    def test__schema_similarity__exactclones__return100(self):
        target = self.df.copy()
        source = self.df.copy()
        scores:Scores = self._calculate_scores(source, target)
        self.assertEqual(scores.overall_schema_similarity, 1.0)
        self.assertEqual(scores.row_similarity, 1.0)
        self.assertEqual(scores.column_similarity, 1.0)
        self.assertEqual(scores.cell_similarity, 1.0)
        self.assertEqual(scores.overall_similarity, 1.0)

    def test__schema_similarity__same_schema_1cell_diff_in_4x5_matrix__return_different_similarities(self):
        target = self.df.copy()
        source = self.df.copy()
        source.at[0, 'dollar_amt'] = 123.46
        scores:Scores = self._calculate_scores(source, target)
        self.assertEqual(scores.overall_schema_similarity, 1.0)
        self.assertEqual(scores.row_similarity, 0.75)
        self.assertEqual(scores.column_similarity, 0.8)
        self.assertEqual(scores.cell_similarity, 0.95)
        self.assertEqual(scores.overall_similarity, 0.975)


if __name__ == '__main__':
    unittest.main()
