import numpy as np
import pandas as pd

# df = pd.read_csv('../Data/student',sep=':')
'''
    class    name  kor  eng  mat  bio
0       1    adam   67   87   90   98
1       1  andrew   45   45   56   98
2       1     ben   95   59   96   88
3       1   clark   65   94   89   98
4       1     dan   45   65   78   98
5       1    noel   78   76   98   89
6       2    paul   87   67   65   56
7       2  walter   89   98   78   78
8       2   oscar  100   78   56   65
9       2  martin   99   89   87   87
10      2    hugh   98   45   56   54
11      2   henry   65   89   87   78
'''

# df = pd.read_csv('../Data/student',delimiter=':')
'''
    class    name  kor  eng  mat  bio
0       1    adam   67   87   90   98
1       1  andrew   45   45   56   98
2       1     ben   95   59   96   88
3       1   clark   65   94   89   98
4       1     dan   45   65   78   98
5       1    noel   78   76   98   89
6       2    paul   87   67   65   56
7       2  walter   89   98   78   78
8       2   oscar  100   78   56   65
9       2  martin   99   89   87   87
10      2    hugh   98   45   56   54
11      2   henry   65   89   87   78
'''

# df = pd.read_csv('../Data/student',sep='::')
'''
C:/pythonproject/day0402/numpytest/day0405/ex03.py:37: ParserWarning: Falling back to the 'python' engine because 
the 'c' engine does not support regex separators (separators > 1 char and different from 
'\s+' are interpreted as regex); you can avoid this warning by specifying engine='python'.
  df = pd.read_csv('../Data/student',sep='::')
'''
# df = pd.read_csv('../Data/student',delimiter='::')
'''
C:/pythonproject/day0402/numpytest/day0405/ex03.py:37: ParserWarning: Falling back to the 'python' engine because 
the 'c' engine does not support regex separators (separators > 1 char and different from 
'\s+' are interpreted as regex); you can avoid this warning by specifying engine='python'.  df = pd.read_csv('../Data/student',delimiter='::')
'''
# 가능은한데 권장하지 않는다고 오류나고 두개의 구분자는 engine = 'python' 으로 바꿔서 써~ 라는 말 #

df = pd.read_csv('../Data/student',delimiter='::',engine='python')
print(df)
'''
    class    name  kor  eng  mat  bio
0       1    adam   67   87   90   98
1       1  andrew   45   45   56   98
2       1     ben   95   59   96   88
3       1   clark   65   94   89   98
4       1     dan   45   65   78   98
5       1    noel   78   76   98   89
6       2    paul   87   67   65   56
7       2  walter   89   98   78   78
8       2   oscar  100   78   56   65
9       2  martin   99   89   87   87
10      2    hugh   98   45   56   54
11      2   henry   65   89   87   78
'''
# 오류 안남

print(df)
'''
   class:name:kor:eng:mat:bio
0          1:adam:67:87:90:98
1        1:andrew:45:45:56:98
2           1:ben:95:59:96:88
3         1:clark:65:94:89:98
4           1:dan:45:65:78:98
5          1:noel:78:76:98:89
6          2:paul:87:67:65:56
7        2:walter:89:98:78:78
8        2:oscar:100:78:56:65
9        2:martin:99:89:87:87
10         2:hugh:98:45:56:54
11        2:henry:65:89:87:78
'''
#  하나의 요소로 읽어들인것


# help를 이용하여 file의 내용을 :으로 구분하여 바람직하게 읽어들이도록 합니다.
# help(pd.read_csv)
'''
read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, 
prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, 
skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, 
verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None,
dayfirst=False, iterator=False, chunksize=None, compression='infer', thousands=None, decimal=b'.', lineterminator=None, 
quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, dialect=None, tupleize_cols=None, 
error_bad_lines=True, warn_bad_lines=True, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None)
    Read a comma-separated values (csv) file into DataFrame.
'''


