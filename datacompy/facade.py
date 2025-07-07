import datacompy

class ComparisonStatus:
    def __init__(self, success: bool, error: str = None, error_type: str = None):
        self.Success: bool = success
        self.Error: str = error
        self.ErrorType: str = error_type

    def __repr__(self):
        return f"ComparisonStatus(success={self.Success}, error='{self.Error}', error_type={self.ErrorType})"

def try_compare(df1, df2, key):
    try:
        compare = datacompy.Compare(df1,df2, join_columns=key, abs_tol=0, rel_tol=0, df1_name='Source', df2_name='Target')
        compare.matches(ignore_extra_columns=False)
        reports, metrics = compare.report()
        status = ComparisonStatus(success=True, error=None)
        return reports, metrics, status
    except Exception as e:
        if str(e).startswith("KEY ERROR:"):
            return None, None, ComparisonStatus(success=False, error=str(e).replace("KEY ERROR:",""), error_type="KEY")
        else:
            # raise e
            return None,None, ComparisonStatus(success=False, error=str(e))