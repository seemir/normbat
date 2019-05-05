# -*- coding: utf-8 -*-

__author__ = 'Samir Adrik'
__email__ = 'samir.adrik@gmail.com'

from normbatt.multivariate_norm.abstract_normality_test import AbstractNormalityTest
from rpy2.robjects import r


class DoornikHansen(AbstractNormalityTest):
    """
    Implementation of the Doornik-Hansen test for multivariate normality

    """

    def __init__(self, df):
        """
        Constructor / Initiate the class

        Parameters
        ----------
        df      : pandas.DataFrame
                  df to be analysed

        """
        super().__init__(df)

    @staticmethod
    def run_dh_test():
        """
        Runs the Doornik-Hansen test for multivariate normality by delegating the task to the
        MVN module in r

        """
        r('res <- mvn(df, mvnTest = "dh")')

    def print_results(self):
        """
        Gets the dh test statistic and p-value

        Returns
        -------
        Out     : tuple
                  (dh test statistic, p-value)

        """

        self.run_dh_test()
        dh = r('as.numeric(res$multivariateNormality["E"])')
        p_dh = r('as.numeric(res$multivariateNormality["p value"])')
        return tuple(list(dh) + list(p_dh))