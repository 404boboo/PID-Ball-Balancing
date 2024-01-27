/**
*@file: hcsr04_sensor.h
*@brief: HC-SR04 ultrasonic distance sensor driver using STM32
*@author:  Ahmed Bouras
*/

#ifndef HCSR04_SENSOR_H
#define HCSR04_SENSOR_H

#ifdef __cplusplus
extern "C" {
#endif

/*Includes-------------------------------------------------------*/
#include "stm32f7xx_hal.h"

/*---------------------------------------------------------------*/

/*Defines and variables------------------------------------------*/

#define MAX_SENSORS 2  // MAX number of sensors
typedef uint32_t TIM_Channel;


/**
  * @brief  The sensor data and configurations structures
  */

struct us_sensor_str
{
	TIM_HandleTypeDef *htim_echo;

	TIM_HandleTypeDef *htim_trig;

	TIM_Channel trig_channel;

	volatile uint32_t distance_cm;
};



/*---------------------------------------------------------------*/

/*Private functions----------------------------------------------*/
/**
*@brief: The sensor initiliazing settings.
*@retval: None
*/


void hc_sr04_init(struct us_sensor_str *us_sensor, TIM_HandleTypeDef *htim_echo, TIM_HandleTypeDef *htim_trig, TIM_Channel channel);
/**
*@brief: The sensor data convert function
*@param:
*@retval: None
*/
uint32_t hc_sr04_convert_us_to_cm(uint32_t distance_us);


/**
*@brief: Calculate the position of the ball depending on two sensors
*@param:
*@retval: None
*/
float CalulatePosition(float dis1, float dis2);

#ifdef __cplusplus
}
#endif

#endif


/******************************************************END OF FILE*********************************************************************/
