#公式：
# 资产=资产+收入-支出
# 负债=负债+应出账款-应收账款
# 净资产=资产-负债
# 要求：
# 在项目文件夹下新建两份 txt 文件，分别记录资产负债与流水账
# 为程序编写账单记录功能与查询功能，允许并提示用户在控制台选择操作
# 每笔交易记录在流水账单，自动添加交易日期，自动结算并更新资产负债表
# 可查询与某公司的贸易往来
# 可查询最近十笔交易记录
# 可查询最新资产负债情况


from datetime import date
dat = str(date.today())

def readbs():
    with open('balance_sheet.txt', encoding='utf-8') as f:
        line = f.readline()
        b_s = line.split()
        readbs = (b_s[1], b_s[2], b_s[3], dat)
        print('asset: %s \nliability: %s \nnet asset: %s \nlatest date: %s \n'%readbs)


def readis():
    with open('income_statement.txt', encoding='utf-8') as f:
        i_s = f.readlines()
        for i in i_s[:3]:
            print(i)


def check_trans(name):
    with open('income_statement.txt', encoding='utf-8') as f:
        i_s = f.readlines()
        record = []
        for i in i_s:
            if name in i:
                record.append(i.split())
    times = len(record)
    print('ttl transactions with %s is %d' % (name, times))
    print()
    for r in record:
        out = (r[5], r[1], r[2], r[3], r[4])
        print('date: %s\nrevenue(w): %s\nexpenditure(w): %s\naccount receivable(w) %s\naccount payable(w): %s\n' % out)


def writerec():
    print('write mode')
    com = input('company name: ')
    rev = input('revenue(w): ')
    exp = input('expenditure(w): ')
    ar = input('account receivable(w): ')
    ap = input('account payable(w): ')

    with open('balance_sheet.txt', 'r+', encoding='utf-8') as f:
        line = f.readline()
        b_s = line.split()
        f.seek(0)
        l = f.read()
        ass = int(b_s[1])
        liab = int(b_s[2])

        ass_new = str(ass + int(rev) - int(exp))
        liab_new = str(liab + int(ap) - int(ar))
        net_new = str(int(ass_new) - int(liab_new))

        b_s_new = ' '.join([dat, ass_new, liab_new, net_new, '\n'])

        f.seek(0)
        f.writelines(b_s_new)
        f.write(l)

    print('record successfully \ncurrent record:')
    print('asset: %s \nliability: %s \nnet asset: %s \nlatest date: %s \n'
          %(ass_new, liab_new, net_new, dat))

    with open('income_statement.txt', 'r+', encoding='utf-8') as f:
        i_s = f.read()
        i_s_new = ' '.join([com, rev, exp, ar, ap, dat, '\n'])
        f.seek(0)
        f.writelines(i_s_new)
        f.write(i_s)


print('1 for read, 2 for write')
mode = int(input('choose a mode: '))
if mode == 1:
    print('read mode: \n1:check latest 3 transactions\n2:check details with certain company\n3:check current b/s\n')
    sub = int(input())
    if sub == 2:
        name = input('company name: ')
        check_trans(name)
    elif sub == 1:
        readis()
    elif sub == 3:
        readbs()
    else:
        pass

elif mode == 2:
    writerec()

else:
    pass










