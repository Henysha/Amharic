# ። አማርኛ ሲ ኮምፓይለር፡፡ መጀመሪያ መሠረት፡፡

import re
import sys

# ። ቃላት ተመልከት (Lexer)
def ቃላት_መለየት(መጻፊያ):
    print("። ቃላት ተመልከት በመጀመር ላይ፡፡")
    ቃላቶች = re.findall(r'\w+|\S', መጻፊያ)
    return ቃላቶች

# ። መዝገበ ቃላት (Parser)
def መዝገበ_ቃላት(ቃላቶች):
    print("። መዝገበ ቃላት በመስራት ላይ፡፡")
    ውጤት = []
    for ቃል in ቃላቶች:
        ውጤት.append(f"ቃል፡ {ቃል}")
    return ውጤት

# ። ኮድ ጀነሬተር (Dummy Code Generator)
def ኮድ_ጀነሬተር(ውጤት):
    print("። ኮድ ጀነሬተር በሥራ ላይ፡፡")
    for መረጃ in ውጤት:
        print(መረጃ)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("። አጠቃቀም፡፡ python አማርኛ_ሲ_ኮምፓይለር.py ፋይል.c")
        sys.exit(1)
    ፋይል_ስም = sys.argv[1]
    try:
        with open(ፋይል_ስም, 'r') as ፋይል:
            መጻፊያ = ፋይል.read()
    except FileNotFoundError:
        print(f"። ስህተት፡፡ ፋይል '{ፋይል_ስም}' አልተገኘም፡፡")
        sys.exit(1)

    ቃላቶች = ቃላት_መለየት(መጻፊያ)
    ውጤት = መዝገበ_ቃላት(ቃላቶች)
    ኮድ_ጀነሬተር(ውጤት)