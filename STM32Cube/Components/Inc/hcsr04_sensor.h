/**
*@file: hcsr04_sensor.h
*@brief: HC-SR04 ultrasonic distance sensor driver using STM32
*@author: Ahmed Bouras
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
extern TIM_HandleTypeDef htim1;
extern TIM_HandleTypeDef htim2;
extern TIM_HandleTypeDef htim_echo;
extern TIM_HandleTypeDef htim_delay;
extern TIM_TypeDef *TIM_Echo;
extern TIM_TypeDef *TIM_Delay;
extern GPIO_TypeDef *GPIO_Trigger;
extern GPIO_TypeDef *GPIO_Echo;
extern uint16_t GPIO_PIN_Trigger, GPIO_PIN_Echo;
extern const float zero_point;



/** 
  * @brief  The sensor data structures definition  
  */
typedef struct hcsr04_data {
	
	float duration_ms;
	float duration_us;
	
	float distance_mm;
	float distance_cm;
	float distance_m;
	float distance_inch;
	
} hcsr04_data_t;

/*---------------------------------------------------------------*/	

/*Private functions----------------------------------------------*/
/**
*@brief: The sensor initiliazing settings.
*@retval: None
*/
void HCSR04_Init(void);

/**
*@brief: HC-SR04 HAL_TIM_PeriodElapsedCallback
*@param: htim pointer to a TIM_HandleTypeDef structure that contains the configurations information for TIM module.
*@retval: None
*/
void HCSR04_TIM_PEC(TIM_HandleTypeDef *htim);

/**
*@brief: The sensor data read function
*@param: HCSR04_DATA pointer to hcsr04_data_t structure that contains data for the sensor.
         HCSR04_DATA -> duration: ms, us, distance: mm, cm, m, inch.
*@retval: None
*/
void HCSR04_GetInfo(hcsr04_data_t *HCSR04_DATA);


#ifdef __cplusplus
}
#endif

#endif


/******************************************************END OF FILE*********************************************************************/
