class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power,
                 average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car):
        dict_rat_coef = self.average_rating / self.distance_from_city_center
        clean_coef = self.clean_power - car.clean_mark
        return round(car.comfort_class * clean_coef * dict_rat_coef, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int):
        av_sum = self.count_of_ratings * self.average_rating
        self.count_of_ratings += 1
        self.average_rating = round((av_sum + mark) / self.count_of_ratings, 1)
