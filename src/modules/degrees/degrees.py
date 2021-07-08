from flask import jsonify

class Degrees():

    def convert_degrees(self, data):
        result = None
        source_unit = data["UnidadeOrigem"].upper()
        target_unit = data["UnidadeDestino"].upper()
        value       = data["Valor"]
        absolute_value = {"K": 273.15, "C":0, "F": 32}

        if source_unit == "C" and target_unit == "K":
            result = self.celsius_to_kelvin(value, absolute_value, target_unit)

        if source_unit == "K" and target_unit == "C":
            result = self.kelvin_to_celsius(value, absolute_value, source_unit)

        if source_unit == "F" and target_unit == "C":
            result = self.fahrenheit_to_celsius(value, absolute_value, source_unit)

        if source_unit == "C" and target_unit == "F":
            result = self.celsius_to_fahrenheit(value, absolute_value, target_unit)

        if source_unit == "K" and target_unit == "F":
            result = self.kelvin_to_fahrenheit(value, absolute_value, source_unit, target_unit)

        if source_unit == "F" and target_unit == "K":
            result = self.fahrenheit_to_kelvin(value, absolute_value, source_unit, target_unit)

        return jsonify(ValorConvertido=result)


    def celsius_to_kelvin(self, value, absolute_value, target_unit):
        return value + absolute_value[target_unit]


    def kelvin_to_celsius(self, value, absolute_value, source_unit):
        return value - absolute_value[source_unit]


    def fahrenheit_to_celsius(self, value, absolute_value, source_unit):
        return (value - absolute_value[source_unit]) / 1.8


    def celsius_to_fahrenheit(self, value, absolute_value, target_unit):
        return ( value * 1.8) + absolute_value[target_unit]


    def kelvin_to_fahrenheit(self, value, absolute_value, source_unit, target_unit):
        return self.celsius_to_fahrenheit(self.kelvin_to_celsius(value, absolute_value, source_unit), absolute_value, target_unit)


    def fahrenheit_to_kelvin(self, value, absolute_value, source_unit, target_unit):
        return self.celsius_to_kelvin(self.fahrenheit_to_celsius(value, absolute_value, source_unit), absolute_value, target_unit)
