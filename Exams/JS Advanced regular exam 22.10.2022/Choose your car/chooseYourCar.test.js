// 58/100 ???

let chooseYourCar = require('./chooseYourCar')
let {assert} = require('chai');

describe('chooseYourCar tests', () => {
    describe('choosing type tests', () => {
        it('year validation', () => {
            assert.throw(chooseYourCar.choosingType('Sedan', 'yellow', 1899), "Invalid Year!");
            assert.throw(chooseYourCar.choosingType('Sedan', 'yellow', 2023), "Invalid Year!");
            assert.throw(chooseYourCar.choosingType('Sedan', 'yellow', 2030), "Invalid Year!");
        });
        it('type validation', () => {
            assert.throw(chooseYourCar.choosingType('Combi', 'yellow', 1900), "This type of car is not what you are looking for.");
            assert.throw(chooseYourCar.choosingType('type2', 'yellow', 2022), "This type of car is not what you are looking for.");
        });
        it('car requirements tests', () => {
            assert.equal(chooseYourCar.choosingType('Sedan', 'yellow', 2010), "This yellow Sedan meets the requirements, that you have.");
            assert.equal(chooseYourCar.choosingType('Sedan', 'yellow', 2020), "This yellow Sedan meets the requirements, that you have.");
            assert.equal(chooseYourCar.choosingType('Sedan', 'yellow', 2009), "This Sedan is too old for you, especially with that yellow color.");
            assert.equal(chooseYourCar.choosingType('Sedan', 'yellow', 2000), "This Sedan is too old for you, especially with that yellow color.");
        });
    });

    describe('brand name tests', () => {
        it('input tests', () => {
            assert.throw(chooseYourCar.brandName('brand 1, brand2', 1), "Invalid Information!");
            assert.throw(chooseYourCar.brandName('brand 1, brand2', '1'), "Invalid Information!");
            assert.throw(chooseYourCar.brandName(10, 1), "Invalid Information!");
            assert.throw(chooseYourCar.brandName({}, 1), "Invalid Information!");
            assert.throw(chooseYourCar.brandName(['brand 1', 'brand2'], {}), "Invalid Information!");
            assert.throw(chooseYourCar.brandName([], false), "Invalid Information!");
            assert.throw(chooseYourCar.brandName([], []), "Invalid Information!");
            assert.throw(chooseYourCar.brandName(false, 2), "Invalid Information!");
            assert.throw(chooseYourCar.brandName(['brand 1', 'brand2'], 2), "Invalid Information!");
            assert.throw(chooseYourCar.brandName(['brand 1', 'brand2'], -3), "Invalid Information!");
        });
        it('remove brand tests', () => {
            assert.equal(chooseYourCar.brandName(['car1', 'car2', 'car3'], 2), "car1, car2");
            assert.equal(chooseYourCar.brandName(['car1'], 0), "");
        });
    });

    describe('CarFuelConsumption tests', () => {
        it('input tests', () => {
            assert.throw(chooseYourCar.carFuelConsumption([], '5'), "Invalid Information!");
            assert.throw(chooseYourCar.carFuelConsumption(6, '5'), "Invalid Information!");
            assert.throw(chooseYourCar.carFuelConsumption(true, {}), "Invalid Information!");
            assert.throw(chooseYourCar.carFuelConsumption(10, false), "Invalid Information!");
            assert.throw(chooseYourCar.carFuelConsumption("", ""), "Invalid Information!");
            assert.throw(chooseYourCar.carFuelConsumption(-5, '5'), "Invalid Information!");
            assert.throw(chooseYourCar.carFuelConsumption(10, -2), "Invalid Information!");
            assert.throw(chooseYourCar.carFuelConsumption(-5, -10), "Invalid Information!");
            assert.throw(chooseYourCar.carFuelConsumption(-100, ['cars']), "Invalid Information!");
        });
        it('consumption tests', () => {
            assert.equal(chooseYourCar.carFuelConsumption(1000, 10), "The car is efficient enough, it burns 1.00 liters/100 km.");
            assert.equal(chooseYourCar.carFuelConsumption(1000, 70), "The car is efficient enough, it burns 7.00 liters/100 km.");
            assert.equal(chooseYourCar.carFuelConsumption(1000, 80), "The car burns too much fuel - 8.00 liters!");
            assert.equal(chooseYourCar.carFuelConsumption(1000, 100), "The car burns too much fuel - 10.00 liters");
        });
    });
})


// решение на колега 100/100

describe('chooseYourCar', () => {
    describe('choosingtype', () => {
        it('tree parameters', () => {
            expect(chooseYourCar.choosingType.length).to.be.equal(3);
        });
        it('errors', () => {
            expect(() => chooseYourCar.choosingType("throw", 'throw2', 1899)).to.throw("Invalid Year!");
            expect(() => chooseYourCar.choosingType("throw", 'throw2', 2023)).to.throw("Invalid Year!");
            expect(() => chooseYourCar.choosingType("throw", 'throw2', 2022)).to.throw("This type of car is not what you are looking for.");
        });
        it('returns', () => {
            let type = "Sedan";
            let color = 'Red';
            expect(chooseYourCar.choosingType(type, color, 2010)).to.be.equal(`This ${color} ${type} meets the requirements, that you have.`);
            expect(chooseYourCar.choosingType(type, color, 2009)).to.be.equal(`This ${type} is too old for you, especially with that ${color} color.`);
 
        });
    });
    describe('brandName', () => {
        it('two parameters', () => {
            expect(chooseYourCar.brandName.length).to.be.equal(2);
        });
        it('errors', () => {
            expect(() => chooseYourCar.brandName("throw", 2)).to.throw("Invalid Information!");
            expect(() => chooseYourCar.brandName([], 2.13)).to.throw("Invalid Information!");
            expect(() => chooseYourCar.brandName(['throw2'], -1)).to.throw("Invalid Information!");
            expect(() => chooseYourCar.brandName(["throw"], 1)).to.throw("Invalid Information!");
        });
        it('returns', () => {
            let brands = ["BMW", "Toyota", "Peugeot"];
            let index = 1;
            expect(chooseYourCar.brandName(brands, index)).to.be.equal(`BMW, Peugeot`);
 
        });
    });
    describe('carFuelConsumption', () => {
        it('two parameters', () => {
            expect(chooseYourCar.carFuelConsumption.length).to.be.equal(2);
        });
        it('errors', () => {
            expect(() => chooseYourCar.carFuelConsumption("throw", 2)).to.throw("Invalid Information!");
            expect(() => chooseYourCar.carFuelConsumption(undefined, 2)).to.throw("Invalid Information!");
            expect(() => chooseYourCar.carFuelConsumption([], 2)).to.throw("Invalid Information!");
            expect(() => chooseYourCar.carFuelConsumption({}, 2)).to.throw("Invalid Information!");
            expect(() => chooseYourCar.carFuelConsumption(true, 2)).to.throw("Invalid Information!");
            expect(() => chooseYourCar.carFuelConsumption(100, "asdsa")).to.throw("Invalid Information!");
            expect(() => chooseYourCar.carFuelConsumption(100, undefined)).to.throw("Invalid Information!");
            expect(() => chooseYourCar.carFuelConsumption(100, [])).to.throw("Invalid Information!");
            expect(() => chooseYourCar.carFuelConsumption(100, {})).to.throw("Invalid Information!");
            expect(() => chooseYourCar.carFuelConsumption(100, true)).to.throw("Invalid Information!");
            expect(() => chooseYourCar.carFuelConsumption(100, -1)).to.throw("Invalid Information!");
            expect(() => chooseYourCar.carFuelConsumption(-1, 20)).to.throw("Invalid Information!");
        });
        it('returns', () => {
            expect(chooseYourCar.carFuelConsumption(1000, 60)).to.be.equal(`The car is efficient enough, it burns 6.00 liters/100 km.`);
            expect(chooseYourCar.carFuelConsumption(1000, 70)).to.be.equal(`The car is efficient enough, it burns 7.00 liters/100 km.`);
            expect(chooseYourCar.carFuelConsumption(100000, 7006)).to.be.equal(`The car burns too much fuel - 7.01 liters!`);
            expect(chooseYourCar.carFuelConsumption(1000, 80)).to.be.equal(`The car burns too much fuel - 8.00 liters!`);
 
        });
    });
});