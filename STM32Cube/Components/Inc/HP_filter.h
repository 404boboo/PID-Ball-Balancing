/*
 * HP_filter.h
 *
 *  Created on: Jan 26, 2024
 *      Author: yazed almazroua
 */

#ifndef INC_HP_FILTER_H_
#define INC_HP_FILTER_H_

typedef struct {

	//Filter coef
	float beta;

	//Filter input
	float inp;

	//Filter output;
	float out;



}IFX_EMA;
void IFX_EMA_Init(IFX_EMA *filt , float beta);
void IFX_EMA_SetBeta(IFX_EMA *filt,float beta);
float IFX_EMA_Update(IFX_EMA *filt,float inp);

#endif /* INC_HP_FILTER_H_ */
