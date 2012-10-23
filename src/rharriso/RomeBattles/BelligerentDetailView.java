package rharriso.RomeBattles;

import java.util.Random;

import android.content.Context;
import android.graphics.BitmapFactory;
import android.graphics.Color;
import android.graphics.PorterDuff.Mode;
import android.graphics.drawable.BitmapDrawable;
import android.util.AttributeSet;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;

public class BelligerentDetailView extends RelativeLayout {
	
	public TextView belligerentText, commanderText, strengthText;
	public ImageView factionIcon;
	
	private BitmapDrawable background;
	
	public BelligerentDetailView(Context context){		
		super(context);		
	}
	
	public BelligerentDetailView(Context context, AttributeSet attrs){		
		super(context, attrs);
	}
	
	@Override
	protected void onFinishInflate (){
		/*
		 * Grab different elements
		 */
		belligerentText = (TextView)findViewById(R.id.belligerentText);
		commanderText	= (TextView)findViewById(R.id.commanderText);
		strengthText	= (TextView)findViewById(R.id.strengthText);
		factionIcon		= (ImageView)findViewById(R.id.factionIcon);
		
		/*
		 * load background
		 */
		this.background = new BitmapDrawable(BitmapFactory.decodeResource(this.getContext().getResources(), R.drawable.breastplate));
		this.setBackgroundDrawable(this.background);
	}
	
	public void loadCoation(Coalition coalition){
		//set other side info
		this.belligerentText.setText(coalition.getAllies());
		this.commanderText.setText(coalition.getCommanders());
		this.strengthText.setText(coalition.getStrength());
		
		Random rand = new Random();
		this.background.setColorFilter(Color.argb(128, rand.nextInt(256), rand.nextInt(256), rand.nextInt(256)), Mode.SCREEN);
	}
}
