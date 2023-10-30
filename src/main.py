from reformator import reformat, lexer
import cppSample
print("testing")
clean_code = reformat(sampleCode)
print(lexer(clean_code))
