class Date:
    def __init__(self, year, month, day):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)

    @property
    def days_in_month(self):
        return 28  # 간단하게 모든 달을 28일로 가정합니다.


    def add_months(self, months):
        months = int(months)
        self.month += months
        while self.month > 12:
            self.year += 1
            self.month -= 12
        return self


    def __eq__(self, other):
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __lt__(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __le__(self, other):
        return (self.year, self.month, self.day) <= (other.year, other.month, other.day)

    def __gt__(self, other):
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)

    def __ge__(self, other):
        return (self.year, self.month, self.day) >= (other.year, other.month, other.day)


def solution(today, terms, privacies):
    answer = []
    today_lst = today.split('.')
    today_obj = Date(*today_lst)
    terms = {term.split()[0]:term.split()[1] for term in terms}
    
    for i, privacy in enumerate(privacies):
        privacy_date, privacy_term = privacy.split()
        privacy_date = Date(*privacy_date.split('.'))
        if today_obj >= privacy_date.add_months(terms[privacy_term]):
            answer.append(i+1)            
    return answer