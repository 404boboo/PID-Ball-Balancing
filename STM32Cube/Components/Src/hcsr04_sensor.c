/**
  * @file    hcsr04_sensor.c
  * @brief   HC-SR04 ultrasonic distance sensor driver
  * @author  Ahmed Bouras
  * @date    28/01/2024
  * @note    The library has been tested on STM32F746ZG Board.
  */

/* Includes ------------------------------------------------------------------*/
#include <hcsr04_sensor.h>

/* Typedef -------------------------------------------------------------------*/

/* Define --------------------------------------------------------------------*/
#define HC_SR04_US_TO_CM_CONVERTER  58

/* Macro ---------------------------------------------------------------------*/
/* Private variables ---------------------------------------------------------*/
/* Public variables ---------------------------------------------------------*/

/* Private functions ---------------------------------------------------------*/

/**
  * @brief  Initializes the HC-SR04 ultrasonic sensor.
  * @param  us_sensor: Pointer to the ultrasonic sensor structure.
  * @param  htim_echo: Pointer to the timer handle for echo.
  * @param  htim_trig: Pointer to the timer handle for trigger.
  * @param  trig_channel: Timer channel for trigger.
  * @retval None
  */
void hc_sr04_init(struct us_sensor_str *us_sensor, TIM_HandleTypeDef *htim_echo, TIM_HandleTypeDef *htim_trig, TIM_Channel trig_channel)
{
    us_sensor->htim_echo = htim_echo;
    us_sensor->htim_trig = htim_trig;
    us_sensor->trig_channel = trig_channel;

    HAL_TIM_IC_Start_IT(us_sensor->htim_echo, TIM_CHANNEL_1 | TIM_CHANNEL_2);
    HAL_TIM_PWM_Start(us_sensor->htim_trig, us_sensor->trig_channel);
}

/**
  * @brief  Converts ultrasonic sensor distance from microseconds to centimeters.
  * @param  distance_us: Distance in microseconds.
  * @retval Distance in centimeters.
  */
float hc_sr04_convert_us_to_cm(float distance_us)
{
    return (distance_us / HC_SR04_US_TO_CM_CONVERTER);
}

/**
  * @brief  Calculates the position based on two distance values.
  * @param  dis1: Distance 1 value.
  * @param  dis2: Distance 2 value.
  * @retval Calculated position value.
  */
int CalulatePosition(float dis1, float dis2)
{
    int position = 0;
    if (dis1 < 29)
        position = dis1;
    else if (dis1 >= 29)
        position = 60 - dis2;
    else if (dis1 >= 29 && dis1 <= 31 && dis2 >= 29 && dis2 <= 31)
        position = 30;
    else if (dis1 >= 29 && dis1 <= 31 && dis2 >= 29 && dis2 <= 31&&dis1>dis2)
    	position = 31;
    else if(dis1 >= 29 && dis1 <= 31 && dis2 >= 29 && dis2 <= 31&&dis1<dis2)
    	position = 29;
    else if (dis1>61 || dis1<0)
    	position = 0;
    else if(dis2>61 || dis2<0)
    	position = 60;
    return position;
}

/******************************************************END OF FILE*********************************************************************/
