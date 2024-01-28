/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2024 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "i2c.h"
#include "tim.h"
#include "usart.h"
#include "gpio.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include <string.h>
#include <stdlib.h>
#include "Servo.h"
#include "stdlib.h"
#include "stm32f7xx_hal.h"
#include "hcsr04_sensor.h"
#include "PID_controller.h"
#include "lcd.h"
#include "lcd_config.h"
#include "Keypad.h"

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */

/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */

float tx_us = 0;     // Time in microseconds
float dx_cm = 0;     // Distance for sensor 1 in centimeters
float dx_cm2 = 0;     // Distance for sensor 2 in centimeters
int position = 0.00; // Position of the ball
int setP = 28;
char KeyPad_Buffer[2];
unsigned char character;
unsigned int user_len= 2;
unsigned int i = 0;
char num;

// Components //

// Sensors
struct us_sensor_str distance_sensor;
struct us_sensor_str distance_sensor2;

// Servos
SERVO_Handle_TypeDef hservo1 = { .PwmOut = PWM_INIT_HANDLE(&htim9, TIM_CHANNEL_1) };
// Buffers //
char position_buffer[5];
uint8_t tx_buffer[4];
const int tx_msg_len = 3;
char text[1];



/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
/* USER CODE BEGIN PFP */
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
{


}
/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
/**
  * @brief  Rx Transfer completed callback.
  * @param  huart UART handle.
  * @retval None
  */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{

}
/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_USART3_UART_Init();
  MX_TIM1_Init();
  MX_TIM9_Init();
  MX_TIM2_Init();
  MX_TIM3_Init();
  MX_I2C1_Init();
  MX_TIM7_Init();
  /* USER CODE BEGIN 2 */

  // Start Sensor 1 & 2
  hc_sr04_init(&distance_sensor, &htim1, &htim2, TIM_CHANNEL_3);
  hc_sr04_init(&distance_sensor2, &htim3, &htim2, TIM_CHANNEL_3);

  // Start Servos
  SERVO_Init(&hservo1);
  SERVO_WritePosition(&hservo1, 90.0f);


 // Start LCD and set up GUI
  LCD_I2C_Init(&hlcd3);
  LCD_I2C_SetCursor(&hlcd3, 0, 0);
  LCD_I2C_printStr(&hlcd3, "Position: ");


  LCD_I2C_SetCursor(&hlcd3, 0, 13);
  LCD_I2C_printStr(&hlcd3, "cm");

  LCD_I2C_SetCursor(&hlcd3, 1, 0);
  LCD_I2C_printStr(&hlcd3, "Set Point: ");

  LCD_I2C_SetCursor(&hlcd3, 1, 14);
  LCD_I2C_printStr(&hlcd3, "cm");

  LCD_I2C_SetCursor(&hlcd3, 1, 11);
  LCD_I2C_printDecInt(&hlcd3, setP);
  KEYPAD_Handle_TypeDef hkeypad = KEYPAD_4x4_INIT_HANDLE(KEYPAD);

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
	 // PID(&hservo1,position,setP);
	  KEYPAD_Handling(&hkeypad,KeyPad_Buffer, 2);

	  // Send Value of Position to LCD
	  LCD_I2C_SetCursor(&hlcd3, 0, 10);
	  LCD_I2C_printDecInt(&hlcd3, position);

	  // Convert position into string
	  sprintf(position_buffer, "%d\r\n", position);

	  // Transmit position through UART
	   HAL_UART_Transmit(&huart3, (uint8_t*)position_buffer, strlen(position_buffer), HAL_MAX_DELAY);

	  HAL_Delay(100);

    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure LSE Drive Capability
  */
  HAL_PWR_EnableBkUpAccess();

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_BYPASS;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLM = 4;
  RCC_OscInitStruct.PLL.PLLN = 216;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV2;
  RCC_OscInitStruct.PLL.PLLQ = 9;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Activate the Over-Drive mode
  */
  if (HAL_PWREx_EnableOverDrive() != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV4;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV4;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_7) != HAL_OK)
  {
    Error_Handler();
  }
}

/* USER CODE BEGIN 4 */
void HAL_TIM_IC_CaptureCallback(TIM_HandleTypeDef *htim)
{
	if(TIM1 == htim->Instance)
	{
		float echo_us;
          // Convert and assign distance
		echo_us = HAL_TIM_ReadCapturedValue(htim, TIM_CHANNEL_2);
		dx_cm = distance_sensor.distance_cm = hc_sr04_convert_us_to_cm(echo_us);
	}

	if(TIM3 == htim->Instance)
	{
		float echo_us;
        // Convert and Assign distance
		echo_us = HAL_TIM_ReadCapturedValue(htim, TIM_CHANNEL_2);
		dx_cm2 = distance_sensor.distance_cm = hc_sr04_convert_us_to_cm(echo_us);
	}

	    // Calculate average distance or perform any other processing
	      position = CalulatePosition(dx_cm, dx_cm2);
		  PID(&hservo1,position,setP);

}

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
