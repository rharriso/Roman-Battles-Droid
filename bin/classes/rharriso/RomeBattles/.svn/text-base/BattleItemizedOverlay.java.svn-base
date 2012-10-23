package rharriso.RomeBattles;

import java.util.ArrayList;

import android.content.Context;
import android.graphics.drawable.Drawable;

import com.google.android.maps.ItemizedOverlay;
import com.google.android.maps.OverlayItem;

public class BattleItemizedOverlay extends ItemizedOverlay<OverlayItem>{
	private ArrayList<OverlayItem> mOverlays = new ArrayList<OverlayItem>();
	public BattleItemizedOverlayListener delegate;	
	
	public BattleItemizedOverlay(Drawable defaultMarker, Context context) {
		super(boundCenterBottom(defaultMarker));
	}
	
	public BattleItemizedOverlay(Drawable defaultMarker) {
		super(boundCenterBottom(defaultMarker));
		
	}
	
	public void addOverlay(OverlayItem overlay){
		mOverlays.add(overlay);
		populate();
	}
	
	@Override
	protected OverlayItem createItem(int i){
		return mOverlays.get(i);		
	}
	
	@Override
	public int size(){
		return mOverlays.size();		
	}
	
	@Override
	protected boolean onTap(int index){
		//to do: some on click functionality
		//the title should be the index of the battle in the parent
		String i = this.getItem(index).getTitle();
		int position = Integer.parseInt(i);
		delegate.battleSelectedAtIndex(position);
		
		return true;		
	}	
}
