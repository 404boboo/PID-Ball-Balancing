/*
 * hc_sr04.h
 *
 *  Created on: Jan 18, 2024
 *  Author: Ahmed Bouras(Ahmed.bouras404@gmail.com)
 *  version: 1.0
 *  Description: Simple driver for ultrasonic distance sensor with I2C: HC-R04
 */

#ifndef INC_HC_SR04_H_
#define INC_HC_SR04_H_

/* Config --------------------------------------------------------------------*/
#define DIST_MAX 250         // Upper limit of the sensor
#define DIST_MIN 10          // Lower limit of the sensor
#define HC_SR04_ITER_MAX 3   // Max iterations in the case measurements are not consistent
#define DISTANCE_E_NOK 0xff
#define SNSR_TOLERANCE 5  //cm

/* Includes ------------------------------------------------------------------*/
#include "stm32f7xx_hal.h"


/* Typedef -------------------------------------------------------------------*/


/* Define --------------------------------------------------------------------*/

// Trigger Pin
#define HC_SR04_Port_Trig                  PORTB
#define HC_SR04_DDR_Trig                   DDR8
#define HC_SR04_Trig_Pin                   PINB4

// Echo Pin

#define HC_SR04_Port_Echo                  PORTD
#define HC_SR04_DDR_Echo                   DDRD
#define HC_SR04_Pin_Echo                   PIND2

// Power Pin

#define HC_SR04_Port_PWR                   PORTB
#define HC_SR04_DDR_PWR                    DDRB
#define HC_SR04_Pin_PWR                    PINB5

#define HC_SR04_PWR_ON           HC_SR04_Port_PWR |= (1<<HC_SR04_PWR_Pin)
#define HC_SR04_PWR_OFF	         HC_SR04_Port_PWR &= ~(1<<HC_SR04_PWR_Pin)

/* Macro ---------------------------------------------------------------------*/

/* Public variables ----------------------------------------------------------*/

/* Public function prototypes ------------------------------------------------*/


void HC_SR04_Init_Init();



#endif /* INC_HC_SR04_H_ */




