/*
 * hc_sr04.c
 *
 *  Created on: Jan 18, 2024
 *  Author: Ahmed Bouras(Ahmed.bouras404@gmail.com)
 *  version: 1.0
 *  Description: Simple driver for ultrasonic distance sensor with I2C: HC-R04
 */



/* Includes ------------------------------------------------------------------*/
#include "hc_sr04.h"

/* Typedef -------------------------------------------------------------------*/

/* Define --------------------------------------------------------------------*/

/* Macro ---------------------------------------------------------------------*/

/* Private variables ---------------------------------------------------------*/

/* Public variables ----------------------------------------------------------*/

/* Private function prototypes -----------------------------------------------*/

/* Private function ----------------------------------------------------------*/

/* Public function -----------------------------------------------------------*/


void HC_SR04_Init()
{

  HAL_GPIO_WritePin(TRIG_PORT, TRIG_PIN, GPIO_PIN_SET);  // pull the TRIG pin HIGH
  __HAL_TIM_SET_COUNTER(&htim1, 0);
  while (__HAL_TIM_GET_COUNTER (&htim1) < 10);  // wait for 10 us
  HAL_GPIO_WritePin(TRIG_PORT, TRIG_PIN, GPIO_PIN_RESET);  // pull the TRIG pin low

  pMillis = HAL_GetTick(); // used this to avoid infinite while loop  (for timeout)
  // wait for the echo pin to go high
  while (!(HAL_GPIO_ReadPin (ECHO_PORT, ECHO_PIN)) && pMillis + 10 >  HAL_GetTick());
  Value1 = __HAL_TIM_GET_COUNTER (&htim1);

  pMillis = HAL_GetTick(); // used this to avoid infinite while loop (for timeout)
  // wait for the echo pin to go low
  while ((HAL_GPIO_ReadPin (ECHO_PORT, ECHO_PIN)) && pMillis + 50 > HAL_GetTick());
  Value2 = __HAL_TIM_GET_COUNTER (&htim1);

  Distance = (Value2-Value1)* 0.034/2;
  HAL_Delay(50);


}


