/**
  * @file    hcsr04_sensor.h
  * @brief   HC-SR04 ultrasonic distance sensor driver using STM32
  * @author  Ahmed Bouras
  * @date    28/01/2024
  */

#ifndef HCSR04_SENSOR_H
#define HCSR04_SENSOR_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes -------------------------------------------------------*/
#include "stm32f7xx_hal.h"

/* Defines and variables ------------------------------------------*/

#define MAX_SENSORS 2  /**< Maximum number of sensors. */
typedef uint32_t TIM_Channel;

/**
  * @brief  The sensor data and configurations structures.
  */
struct us_sensor_str
{
    TIM_HandleTypeDef *htim_echo;   /**< Timer handle for echo. */
    TIM_HandleTypeDef *htim_trig;   /**< Timer handle for trigger. */
    TIM_Channel trig_channel;       /**< Timer channel for trigger. */
    volatile uint32_t distance_cm;  /**< Distance in centimeters. */
};

/* Private functions ---------------------------------------------*/

/**
  * @brief  Initializes sensor settings.
  * @param  us_sensor: Pointer to the ultrasonic sensor structure.
  * @param  htim_echo: Pointer to the timer handle for echo.
  * @param  htim_trig: Pointer to the timer handle for trigger.
  * @param  channel: Timer channel for trigger.
  * @retval None
  */
void hc_sr04_init(struct us_sensor_str *us_sensor, TIM_HandleTypeDef *htim_echo, TIM_HandleTypeDef *htim_trig, TIM_Channel channel);

/**
  * @brief  Converts ultrasonic sensor distance from microseconds to centimeters.
  * @param  distance_us: Distance in microseconds.
  * @retval Distance in centimeters.
  */
uint32_t hc_sr04_convert_us_to_cm(uint32_t distance_us);

/**
  * @brief  Calculates the position based on two distance values.
  * @param  dis1: Distance 1 value.
  * @param  dis2: Distance 2 value.
  * @retval Calculated position value.
  */
int CalulatePosition(int dis1, int dis2);

#ifdef __cplusplus
}
#endif

#endif

/******************************************************END OF FILE*********************************************************************/
