#!/usr/bin/env bash

echo ""
echo -e "$ python -um sample_package.main\n"
python -um sample_package.main

echo -e "\n"
echo -e "$ python -um sample_package.sub_package.demo\n"
python -um sample_package.sub_package.demo
