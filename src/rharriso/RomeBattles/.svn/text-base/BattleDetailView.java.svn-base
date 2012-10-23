package rharriso.RomeBattles;

import android.content.Context;
import android.util.AttributeSet;
import android.util.Log;
import android.widget.LinearLayout;

public class BattleDetailView extends LinearLayout{

	BelligerentDetailView belligerentDetailView1;
	BelligerentDetailView belligerentDetailView2;
	
	public BattleDetailView(Context context){		
		super(context);
	}
	
	public BattleDetailView(Context context, AttributeSet attrs){		
		super(context, attrs);
	}
	
	/*
	 * (non-Javadoc)
	 * @see android.view.View#onFinishInflate()
	 */
	protected void onFinishInflate (){
		Log.d("BattleDetailView", "BattleDetailView: onFinishInflate");	
		
		belligerentDetailView1 = (BelligerentDetailView)findViewById(R.id.belligerentDetailView1);
	 	belligerentDetailView2 = (BelligerentDetailView)findViewById(R.id.belligerentDetailView2);
	}
	
	public void showBattle(Battle battle){
		//set first side info
		belligerentDetailView1.loadCoation(battle.getCoalition1());
		belligerentDetailView2.loadCoation(battle.getCoalition2());
		
		int rando = (int) Math.floor(5*Math.random());
		
		switch(rando){
			case 0:
				belligerentDetailView1.factionIcon.setImageResource(R.drawable.aequi);
				belligerentDetailView2.factionIcon.setImageResource(R.drawable.dacia);
				break;
			case 1:
				belligerentDetailView1.factionIcon.setImageResource(R.drawable.carthage);
				belligerentDetailView2.factionIcon.setImageResource(R.drawable.etruscans);
				break;
			case 2:
				belligerentDetailView1.factionIcon.setImageResource(R.drawable.selucid);
				belligerentDetailView2.factionIcon.setImageResource(R.drawable.sassanids);
				break;
			case 3:
				belligerentDetailView1.factionIcon.setImageResource(R.drawable.samnium);
				belligerentDetailView2.factionIcon.setImageResource(R.drawable.parthians);
				break;
			case 4:
				belligerentDetailView1.factionIcon.setImageResource(R.drawable.macedon);
				belligerentDetailView2.factionIcon.setImageResource(R.drawable.germans);
				break;
			default:
				belligerentDetailView1.factionIcon.setImageResource(R.drawable.gauls);
				belligerentDetailView2.factionIcon.setImageResource(R.drawable.goths);
				break;
		}
		
		this.setVisibility(0);
	}
}
