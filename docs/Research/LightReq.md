# Light Requirements
## Spectrum
Over their lifecycles, plants will typically require two different levels of light exposure. During the young vegetative growth period, they require blue light exposure: wavelengths of ~400-500nm or ~5000-7500 Kelvin. During the mature flowering or fruit-bearing growth period, they require red light exposure: wavelengths of 620-780 nm or 2000-3000 Kelvin. ([1]).

The SECO project is completely oriented towards rearing seedlings. The limited space of a desktop greenhouse should be entirely dedicated to supporting plants in their most important and vulnerable stage, from seed to seedling. Therefore, only blue lighting is required for SECO.

In limited doses, ultraviolet radiation can support plant growth. UV-A (315-400nm) leads to smaller but stockier plants ([2]). These plants are more robust and easily survive transplantation into greenhouses.

However, shorter UV-B wavelengths (280-315nm) generally have damaging effects on plant growth, DNA, and photosynthesis ([2]). In very small amounts, these wavelengths can prevent fungal infections([1]); however, by filtering air and water and operating in closed environment, these risks should be minimized.

Very short UV-C radiation (100-280nm) is harmful to plants ([1]).

## Luminosity
The average insolation requirement for plants, including peppers, is typically given as 5000-7500 lumens per square foot. However, this is an average value. During the vegetative stage, plants need approximately 2000-3000 lumens per square foot, while during the flowering stage they require 7500-1000 lumens per square foot for optimal fruit growth. For vegetative seedlings, the SECO needs to be able to provide 2000-3000 lumens per square foot ([3]).

## Length of Time 
Plants in the vegetative state require at least 13 hours of light per day. They enjoy up to 18 hours a day, with some sources even reporting 24 hours a day is acceptable and effective. Receiving under 13 hours of light per day will cause the plant to enter the flowering stage, although this can be reverted by increasing the light level again. ([4]).

# LED Requirements
To summarize, the requirements are for mild 315-400nm lighting and moderate 400-500nm lighting, totaling up to 2000-3000 lumens.

Due to having a supply on-hand, Epiled LEDs will be used. The colors will be Ultraviolet, Royal Blue, and Bright Blue (380-390nm, 440-450nm, 460-470nm). These LEDs are rated for a luminous flux output of 30-50 lumens, with the Ultraviolet being slightly lower [need more info]. To achieve at least 2500 lumens on average, assuming an average of 40 lumens per LED, 66 LEDs will produce 2640 lumens or more.

As ultraviolet light is the least important and mid-range blue the most important, the distribution will be 12 Ultraviolet LEDs, 30 Royal Blue LEDs, and 24 Bright Blue LEDs.

All LEDs have a maximum forward current of 750 mA, also corresponding to their brightest output.

| LED          | Wavelength (nm) | Count | Forward Current (mA) | Forward Voltage (V) | Total Voltage | Total Power    |
|:------------:|:---------------:|:-----:|:--------------------:|:-------------------:|:-------------:|:--------------:|
| Ultraviolet  | 380-390         | 12    | 750                  | 3.5 - 4.5           | Up to 54 V    | Up to 40.5 W   |
| Royal Blue   | 440-450         | 30    | 750                  | 3.4 - 4             | Up to 120 V   | Up to 90 W     |
| Bright Blue  | 460-470         | 24    | 750                  | 3.4 - 4             | Up to 96 V    | Up to 72 W     |
| Total        | 380-470         | 66    | 750                  | 3.4 - 4.5           | Up to 270 V   | Up to 202.5 W  |

These LEDs are driven in series. To be able to precisely control the luminosity, the circuit could either have switches to bypass the latter LEDs in the series; or, multiple LED circuits could be created and turned on/off at will. The former option would require fewer drivers in total, but a a more complicated switching circuit.

FutureEden sells a 40W, 30-50V, 800 mA power supply. To strictly meet the wattage requirements, five would be required; to strictly meet the voltage requirements (assuming ~40V average output), at least seven could be required. Further research needs to be done on optimal LED drivers.

# Additional Reading 
- https://thepoolgardener.com/plant-growth-stages-of-pepper-plants/
- https://www.nasa.gov/content/growing-plants-in-space

# Sources 
[1]: https://theindoornursery.com/blog/full-spectrum-light-for-plants/
[2]: https://www.sciencedirect.com/science/article/pii/S0304423819309963
[3]: https://www.blogarama.com/home-and-garden-blogs/1330395-best-grow-tent-for-indoor-gardening-blog/41134159-many-led-lumens-per-plant-precise-amount
[4]: https://growsupplyshop.com/blogs/news/how-much-light-for-vegetative-flowering-stages-indoors

# Parts 
- FutureEden 3W Ultraviolet LED (380-390nm EPILED)
- FutureEden 3W Royal Blue LED (440-450nm EPILED)
- [FutureEden 3W Bright Blue LED (EPILED 460nm)](https://futureeden.co.uk/collections/blue-high-power-leds-460-470nm-epiled-bridgelux/products/3w-bright-blue-led-epiled-460-470nm-with-star-pcb-heatsink)
- [FutureEden 40W Constant Current LED Driver (800mA) 30-50v](https://futureeden.co.uk/collections/constant-current-led-drivers-power-supplies/products/40w-constant-current-led-driver-800ma-30-50v?variant=36230625612)

