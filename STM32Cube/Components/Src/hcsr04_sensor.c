/**
*@file: hcsr04_sensor.c
*@brief: HC-SR04 ultrasonic distance sensor driver
*@author: Ahmed Bouras
* The library has been tested on STM32F746ZG Board.
*/

/*Includes---------------------------------------------------------*/
#include "hcsr04_sensor.h"



/*Defines and variables--------------------------------------------*/
TIM_HandleTypeDef htim_echo;
TIM_HandleTypeDef htim_delay;
TIM_TypeDef *TIM_Echo;
TIM_TypeDef *TIM_Delay;
GPIO_TypeDef *GPIO_Trigger;
GPIO_TypeDef *GPIO_Echo;
uint16_t GPIO_PIN_Trigger, GPIO_PIN_Echo;
const float zero_point;

/*Private functions------------------------------------------------*/
/**
*@brief: The sensor initiliazing settings.
*@retval: None
*/

void HCSR04_Init(void)
{
	htim_echo        = htim1;         // htim Echo pin.
	  TIM_Echo         = TIM1;          // TIM Echo pin.
		htim_delay       = htim2;	        // htim delay for Trig
		TIM_Delay        = TIM2;          // TIM2 delay for Trig

		GPIO_Trigger     = GPIOA;          // Trigger Port.
		GPIO_PIN_Trigger = GPIO_PIN_6;    //  Trigger Pin.
		GPIO_Echo        = GPIOE;         // Echo Port.
		GPIO_PIN_Echo    = GPIO_PIN_9;   // Echo Pin.
	
	HAL_GPIO_WritePin(GPIO_Trigger, GPIO_PIN_Trigger, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIO_Echo, GPIO_PIN_Echo, GPIO_PIN_RESET);
	 
  HAL_TIM_Base_Start_IT(&htim_echo);
	HAL_TIM_Base_Start_IT(&htim_delay);
}

/**
*@brief: HC-SR04 HAL_TIM_PeriodElapsedCallback function
*@param: htim pointer to a TIM_HandleTypeDef structure that contains the configuration information for TIM module.
*@retval: None
*/
void HCSR04_TIM_PEC(TIM_HandleTypeDef *htim)
{

	htim_echo        = htim1;         // htim Echo pin.
	  TIM_Echo         = TIM1;          // TIM Echo pin.
		htim_delay       = htim2;	        // htim delay for Trig
		TIM_Delay        = TIM2;          // TIM2 delay for Trig

		GPIO_Trigger     = GPIOA;          // Trigger Port.
		GPIO_PIN_Trigger = GPIO_PIN_6;    //  Trigger Pin.
		GPIO_Echo        = GPIOE;         // Echo Port.
		GPIO_PIN_Echo    = GPIO_PIN_9;   // Echo Pin.
	
	if(htim->Instance == TIM_Delay)
		__HAL_TIM_CLEAR_FLAG(&htim_delay, TIM_FLAG_UPDATE);            //Clear TIM_Delay UPDATE event Flag.
	
	else if(htim->Instance == TIM_Echo)
		{
			HAL_GPIO_WritePin(GPIO_Echo, GPIO_PIN_Echo, GPIO_PIN_RESET); //Reset Echo
	    __HAL_TIM_CLEAR_FLAG(&htim_echo, TIM_FLAG_UPDATE);           //Clear TIM_Echo UPDATE event Flag.
	  }
}

/**
*@brief: The sensor data read function
*@param: HCSR04_DATA pointer to hcsr04_data_t structure that contains data for the sensor.
         HCSR04_DATA -> duration: ms, us, distance: mm, cm, m, inch.   
*@retval: None
*/
void HCSR04_GetInfo(hcsr04_data_t *HCSR04_DATA)
{
	static volatile float duration = 0, distance = 0;

	htim_echo        = htim1;         // htim Echo pin.
	  TIM_Echo         = TIM1;          // TIM Echo pin.
		htim_delay       = htim2;	        // htim delay for Trig
		TIM_Delay        = TIM2;          // TIM2 delay for Trig

		GPIO_Trigger     = GPIOA;          // Trigger Port.
		GPIO_PIN_Trigger = GPIO_PIN_6;    //  Trigger Pin.
		GPIO_Echo        = GPIOE;         // Echo Port.
		GPIO_PIN_Echo    = GPIO_PIN_9;   // Echo Pin.
	
	

		HAL_GPIO_WritePin(GPIO_Echo, GPIO_PIN_Echo, GPIO_PIN_SET);        //Set blue led. Used for monitoring
		HAL_GPIO_WritePin(GPIO_Trigger, GPIO_PIN_Trigger, GPIO_PIN_SET);  //Set trigger pin, orange led. Used for monitoring
		
	  /*----10us delay by default:TIM2-----------------------------*/
    __HAL_TIM_SetCounter(&htim_delay, 0);
	  while(__HAL_TIM_GET_FLAG(&htim_delay, TIM_FLAG_UPDATE) != SET)
	  {	
			
	  }
    /*-----------------------------------------------------------*/

    HAL_GPIO_WritePin(GPIO_Trigger, GPIO_PIN_Trigger, GPIO_PIN_RESET); //Reset trigger pin, orange led.
    
	
		while(__HAL_TIM_GET_FLAG(&htim_echo,TIM_FLAG_TRIGGER) != RESET && __HAL_TIM_GET_FLAG(&htim_echo, TIM_FLAG_UPDATE) != SET)
		{	
			
			duration = __HAL_TIM_GetCounter(&htim_echo);        //Get TIM_Echo(default:TIM1) counter value(default:us) as long as there is Echo signal(rising edge).					
			__HAL_TIM_SetCounter(&htim_echo, 0);                //Reset counter value
			__HAL_TIM_CLEAR_FLAG(&htim_echo, TIM_FLAG_TRIGGER); //Clear TIM_Echo Trigger Flag.
		
		}
		
				
		//X=V*t, X=distance_cm, V=0.0343cm/us, t=(transmission + reception time)/2 us
		distance = (duration/2)*(float)0.0343; //sound speed = 343m/s = 0.0343cm/us
		distance -= zero_point;                //subtract the zero point and then, the distance(default:cm) equals from the zero point to object.
	
	  HCSR04_DATA->distance_cm = distance;
		HCSR04_DATA->distance_mm = distance*10;
		HCSR04_DATA->distance_m = distance/100;
		HCSR04_DATA->distance_inch = distance/(float)2.54;
		
		HCSR04_DATA->duration_us = duration;
		HCSR04_DATA->duration_ms = duration/1000;
}


/******************************************************END OF FILE*********************************************************************/
