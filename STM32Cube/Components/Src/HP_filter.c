/*
 * HP_filter.c
 *
 *  Created on: Jan 26, 2024
 *      Author: yazed almazroua
 */
#include "HP_filter.h"
void IFX_EMA_Init(IFX_EMA *filt , float beta){

	//set filter coef
	IFX_EMA_SetBeta(filt,beta);

	//clear filter input
	filt->inp = 0.0f;

	//clear filter output

	filt->out = 0.0f;



}
void IFX_EMA_SetBeta(IFX_EMA *filt,float beta){

	//clamp beta 0 to 1.00
	if(beta > 1.0f){
		beta = 1.0f;
	}
	else if(beta <0.0f){
		beta = 0.0f;
	}
	//set beta coef
	filt->beta = beta;
}
float IFX_EMA_Update(IFX_EMA *filt,float inp){

	//compute current output sample
	filt->out = 0.5f *(2.0f - filt->beta) * (inp - filt->inp) + (1.0f - filt->beta) * filt->out;

	//store current filter input for next output

	filt->inp = inp;

	return filt->out;
}

