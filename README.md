Prerequisites:

pip install requests
pip install yamlordereddictloader
pip install httplib
pip install yaml

How to run :
    python RestApi.py

Settings:

test.yml
    Select the tests to be conducted by providing the depth to which the RestAPI is to be tested.
    Required test cases to run can be controlled using the test.yml page, Framework will run the cases thats mentioned in the .yml page.
    for eg: if you want to run only one test case you just need to mention that case in the yml file.
    To add new test case, add it in to the yml file and include test procedure inside RestApy.py

config.yml

    Select the configuration parameters of tne test such as url

Test traces can be found under the file name : Log.log , PASS/FAIL statuses are also included in the Trace . 
