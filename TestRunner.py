from behave import __main__ as runner
import sys
import os

#9941625522


if __name__ == '__main__':
    sys.stdout.flush()

    FeatureFilePath = 'Features'
    Tags = ' --tags=Regression --tags=Sanity '
    AllureReportPath = " -f allure_behave.formatter:AllureFormatter -o reports"
    behaveOptions = ' --summary --capture '
    run = FeatureFilePath+Tags+AllureReportPath+behaveOptions
    runner.main(run)

    reportingdir = os.getcwd()+"\\reports"
    os.system('cmd /c "allure serve "'+reportingdir)

    #

    '''
    Tags = ' --tags=Regression ' #only regressiom
    Tags = ' --tags=-Regression ' #except regression
    Tags = ' --tags=Regression,Sanity '#Or
    Tags = ' --tags=Regression --tags=Sanity '
    
    
    
    
    '''