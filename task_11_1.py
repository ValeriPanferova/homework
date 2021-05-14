class Data:
    def __init__(self, date_month_year):
        self.date_month_year = date_month_year.split('-')

    @classmethod
    def extraction(cls, day_month_year):
        try:
            day, month, year = [int(i) for i in day_month_year.split('-')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return 'Указана неправильная дата!'

    @staticmethod
    def validate(data):
        try:
            day, month, year = data.split('-')
            (int(year), int(month), int(day))
            return 'Дата указана корректно!'
        except ValueError:
            return 'Указана неправильная дата!'


print(Data.validate('13-05-2021'))
print(Data.extraction('25-02'))
