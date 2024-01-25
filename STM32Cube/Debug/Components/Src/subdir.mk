################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (11.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Components/Src/PID_controller.c \
../Components/Src/Servo.c \
../Components/Src/hcsr04_conf.c \
../Components/Src/hcsr04_sensor.c \
../Components/Src/pwm.c 

OBJS += \
./Components/Src/PID_controller.o \
./Components/Src/Servo.o \
./Components/Src/hcsr04_conf.o \
./Components/Src/hcsr04_sensor.o \
./Components/Src/pwm.o 

C_DEPS += \
./Components/Src/PID_controller.d \
./Components/Src/Servo.d \
./Components/Src/hcsr04_conf.d \
./Components/Src/hcsr04_sensor.d \
./Components/Src/pwm.d 


# Each subdirectory must supply rules for building sources it contributes
Components/Src/%.o Components/Src/%.su Components/Src/%.cyclo: ../Components/Src/%.c Components/Src/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m7 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F746xx -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -I"C:/Users/ahmed/OneDrive/Desktop/Projects/PID-Ball-Balancing/STM32Cube/Components/Inc" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Components-2f-Src

clean-Components-2f-Src:
	-$(RM) ./Components/Src/PID_controller.cyclo ./Components/Src/PID_controller.d ./Components/Src/PID_controller.o ./Components/Src/PID_controller.su ./Components/Src/Servo.cyclo ./Components/Src/Servo.d ./Components/Src/Servo.o ./Components/Src/Servo.su ./Components/Src/hcsr04_conf.cyclo ./Components/Src/hcsr04_conf.d ./Components/Src/hcsr04_conf.o ./Components/Src/hcsr04_conf.su ./Components/Src/hcsr04_sensor.cyclo ./Components/Src/hcsr04_sensor.d ./Components/Src/hcsr04_sensor.o ./Components/Src/hcsr04_sensor.su ./Components/Src/pwm.cyclo ./Components/Src/pwm.d ./Components/Src/pwm.o ./Components/Src/pwm.su

.PHONY: clean-Components-2f-Src

