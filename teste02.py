import xlrd


def xlread(arq_xls):
    xls = xlrd.open_workbook(arq_xls)
    plan = xls.sheets()[0]

    for i in range(plan.nrows):
        yield plan.row_values(i)


for line in xlread("teste.xlsx"):
    print(line)
