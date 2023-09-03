def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    males = int(input('Enter Number of Males: '))
    females = int(input('Enter Number of Females: '))
    total_stu = int(males) + int(females)
    m_perc = (males/total_stu) * 100
    f_perc = (females/total_stu) * 100
    print(f'The percentage of male and females: \t {m_perc} \t {f_perc}')
    print(total_stu)
    print(f'percentages \t {f_perc:.2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
