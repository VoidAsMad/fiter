from fiter import utils
import math

class Conversion:

    def format(self, number: str, format: str = "") -> str:
        """
        단위를 추가합니다.<br> `format` 파라미터는 반환값에 `format`문자열을 붙여 반환합니다.
        """
        result = ""
        sign = ""
        power = 100
        number = float(number)

        if number == 0:
            result = "0"
        elif number < 0:
            sign = "-"
            number = abs(number)

        for i in utils.format_list:
            if number >= math.pow(10, power):
                result += f" {int(number // math.pow(10, power)):,}{i}"
                number = number % math.pow(10, power)

            if power == 100:
                power -= 32
            else:
                power -= 4

        result = result.strip()
        if len(result) >= 1:
            return sign + result + " " + format
        else:
            return number
