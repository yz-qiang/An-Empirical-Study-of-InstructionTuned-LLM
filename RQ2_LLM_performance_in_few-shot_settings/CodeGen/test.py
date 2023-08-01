import re
def assert_criteria(predict) -> bool:
        flag = True
        # should contain code
        # Block
        if not "```" in predict:
            flag = False
        else:
            code_pattern = r'.*```.*assert.*(```)?.*'
            if re.match(code_pattern, predict, flags=re.I|re.DOTALL):
                flag = True
            else:
                flag = False
            return flag

        # single line
        single_line_code_pattern = r'((org.junit.)?(Assert.)?\s*assert[A-Za-z\s]+\(+)+[\s\S]+$'
        if re.match(single_line_code_pattern, predict, flags=re.I):
            flag = True
        assert_fail_pattern = r'((org.junit.)?(Assert.)?\s*fail[A-Za-z\s]*\(+)+[\s\S]+$'
        if re.match(assert_fail_pattern, predict, flags=re.I):
            flag = True

        # In tag
        # if predict.startswith("<assertplaceholder>") and len(predict)>30:
        #     flag = True
        assert_placeholder_pattern = r'<assertplaceholder>.*(?<!<\/)assert.*(</assertplaceholder>)?[\s\S]*$'
        if re.match(assert_placeholder_pattern, predict, flags=re.I|re.DOTALL):
            flag = True

        if len(re.findall("assertplaceholder", predict)) > 3:
            flag = False

        # too short
        # if len(nltk.word_tokenize(predict)) < 3:
        #     flag = False
        return flag
predict = "\n {\n \"code\": 0,\n \"message\": \"Success\",\n \"mutations\": 100,\n \"mutationsDetected\": 100,\n \"coverage\": 100\n }\n */\n\npublic class Test {\n    @Test\n    public void test() {\n        assertEquals(0, 0);\n    }\n}\n"
print(assert_criteria(predict))