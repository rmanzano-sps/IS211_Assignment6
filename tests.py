import unittest
from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit
import numpy


class TemperatireConversionTest(unittest.TestCase):

    temperature_comparison = []
    counter = 0

    for celsius in numpy.arange(-270.00,501.00, 10.00):
        temperature_comparison.append([celsius])

    for fahrenheit in numpy.arange(-454.00,933.00, 18.00):
        temperature_comparison[counter].append(fahrenheit)
        counter = counter + 1

    counter = 0

    for kelvin in numpy.arange(3.15,774.15, 10):
        temperature_comparison[counter].append(kelvin)
        counter = counter + 1

    temperature_comparison.insert(0, [-273.15, -459.67, 0.00])


    def test_convertCelsiusToKelvin(self):
        for temp in self.temperature_comparison:
            print(temp[0])
            result = convertCelsiusToKelvin(temp[0])
            self.assertEqual(temp[1], result, 'This is an error')

    def test_convertCelsiusToFahrenheit(self):
        for temp in self.temperature_comparison:
            result = convertCelsiusToFahrenheit(temp[0])
            self.assertEqual(temp[2], result)


if __name__ == '__main__':
    unittest.main()
