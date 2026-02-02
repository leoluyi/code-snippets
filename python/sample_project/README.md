# Python - What happened when importing packages

https://blog.csdn.net/nigelyq/article/details/78930330

### Run as module

```
$ python -um sample_package.main

>> sys.argv=['/Users/leoluyi/Dropbox/leo_works/[Python]/_python_notes/sample_project/sample_package/main.py']
>> sys.path=['', '/Users/leoluyi/.pyenv/versions/3.6.8/lib/python36.zip', '/Users/leoluyi/.pyenv/versions/3.6.8/lib/python3.6', '/Users/leoluyi/.pyenv/versions/3.6.8/lib/python3.6/lib-dynload', '/Users/leoluyi/.pyenv/versions/3.6.8/lib/python3.6/site-packages']
>> __file__="/Users/leoluyi/Dropbox/leo_works/[Python]/_python_notes/sample_project/sample_package/main.py"
>> __name__="__main__"
>> __package__="sample_package"
--------------------------------------------------------------------
>> __file__="/Users/leoluyi/Dropbox/leo_works/[Python]/_python_notes/sample_project/sample_package/my_module.py"
>> __name__="sample_package.my_module"
>> __package__="sample_package"
--------------------------------------------------------------------
Hello!


$ python -um sample_package.sub_package.demo

>> sys.argv=['/Users/leoluyi/Dropbox/leo_works/[Python]/_python_notes/sample_project/sample_package/sub_package/demo.py']
>> __file__="/Users/leoluyi/Dropbox/leo_works/[Python]/_python_notes/sample_project/sample_package/sub_package/demo.py"
>> __name__="__main__"
>> __package__="sample_package.sub_package"
--------------------------------------------------------------------
>> __file__="/Users/leoluyi/Dropbox/leo_works/[Python]/_python_notes/sample_project/sample_package/my_module.py"
>> __name__="sample_package.my_module"
>> __package__="sample_package"
--------------------------------------------------------------------
Hello!
```

### Run as script

```
$ python run.py

>> sys.argv=['run.py']
>> sys.path=['/Users/leoluyi/Dropbox/leo_works/[Python]/_python_notes/sample_project', '/Users/leoluyi/.pyenv/versions/3.6.8/lib/python36.zip', '/Users/leoluyi/.pyenv/versions/3.6.8/lib/python3.6', '/Users/leoluyi/.pyenv/versions/3.6.8/lib/python3.6/lib-dynload', '/Users/leoluyi/.pyenv/versions/3.6.8/lib/python3.6/site-packages']
>> __file__="run.py"
>> __name__="__main__"
>> __package__="None"
>> __file__="/Users/leoluyi/Dropbox/leo_works/[Python]/_python_notes/sample_project/sample_package/sub_package/demo.py"
>> __name__="sample_package.sub_package.demo"
>> __package__="sample_package.sub_package"
--------------------------------------------------------------------
>> __file__="/Users/leoluyi/Dropbox/leo_works/[Python]/_python_notes/sample_project/sample_package/my_module.py"
>> __name__="sample_package.my_module"
>> __package__="sample_package"
--------------------------------------------------------------------
Hello!
```
