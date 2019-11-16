from sympy import *

moto01=Symbol('moto01')
moto02=Symbol('moto02')
moto03=Symbol('moto03')
car01=Symbol('car01')
car02=Symbol('car02')
car03=Symbol('car03')
suzuki=Symbol('suzuki')
bmw=Symbol('bmw')
joe=Symbol('joe')
frank=Symbol('frank')
mary=Symbol('mary')
gary=Symbol('gary')
john=Symbol('john')

print solve([moto01+suzuki+joe-45,moto01+suzuki+frank-40,moto02+suzuki+joe-20,car01+suzuki+mary-15,car01+bmw+mary-20,moto02+bmw+mary-10,moto01+bmw+gary-65,car02+bmw+gary-110,moto03+suzuki+john-45,car03+suzuki+john-25,car03+bmw+frank-45],[moto01,moto02,moto03,car01,car02,car03,suzuki,bmw,joe,frank,mary,gary,john])
