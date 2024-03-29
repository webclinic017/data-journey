
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Any results you write to the current directory are saved as output.
import pandas as pd
s = pd.Series(['11.0', '20', -30], name='example')
s
pd.to_numeric(s, downcast='float')
pd.to_numeric(s, downcast='signed')
s = pd.Series(['mistake', '11.0', '20', -3])
s
s = pd.to_numeric(s, errors='coerce')
s
s.dtype