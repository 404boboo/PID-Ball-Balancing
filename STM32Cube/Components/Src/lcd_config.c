/**
  ******************************************************************************
  * @file    lcd_config.c
  * @author  Konrad Marchewka
  * @version V1.0
  * @date    23-Jan-2024
  * @brief   Simple HD44780 driver library for STM32F7 configuration file.
  *
  ******************************************************************************
  */
  
/* Includes ------------------------------------------------------------------*/
#include "lcd.h"
#include "lcd_config.h"
#include "main.h"
#include "i2c.h"

#ifdef LCD_USE_TIMER
#include "tim.h"
#endif



LCD_I2C_HandleTypeDef hlcd3 = {
    .I2C = &hi2c1,
    .Address = 0x27,  // PCF8574T (for all jumpers OPEN)
    .Timeout = 100,
    .Timer = &htim7
};

