/**
*@file: hcsr04_sensor.c
*@brief: HC-SR04 ultrasonic distance sensor driver
*@author: Ahmed Bouras
* The library has been tested on STM32F746ZG Board.
*/
/* Includes ------------------------------------------------------------------*/
#include <hcsr04_sensor.h>
/* Typedef -------------------------------------------------------------------*/

/* Define --------------------------------------------------------------------*/
#define HC_SR04_US_TO_CM_CONVERTER	58

/* Macro ---------------------------------------------------------------------*/

/* Public variables ----------------------------------------------------------*/

/*Private functions------------------------------------------------*/

void hc_sr04_init(struct us_sensor_str *us_sensor, TIM_HandleTypeDef *htim_echo, TIM_HandleTypeDef *htim_trig, TIM_Channel trig_channel)
{
	us_sensor->htim_echo = htim_echo;
	us_sensor->htim_trig = htim_trig;
	us_sensor->trig_channel = trig_channel;

	HAL_TIM_IC_Start_IT(us_sensor->htim_echo, TIM_CHANNEL_1 | TIM_CHANNEL_2);
	HAL_TIM_PWM_Start(us_sensor->htim_trig, us_sensor->trig_channel);
}

uint32_t hc_sr04_convert_us_to_cm(uint32_t distance_us)
{
	return (distance_us / HC_SR04_US_TO_CM_CONVERTER);
}
int position(float dis1, float dis2, float pos)
{
 pos = 0;
if (dis1<29){
    pos = dis1;
}
else if(dis1 >=29 )
{
    pos = 60- dis2;
}
else if (dis1>= 29 && dis1 <= 31 && dis2 >= 29 && dis2 <= 31){
    pos = 30;
}
return pos;
}
/******************************************************END OF FILE*********************************************************************/
