package rharriso.RomeBattles;

import java.io.IOException;
import java.io.InputStream;
import java.io.StringWriter;
import java.util.ArrayList;
import java.util.List;

import org.apache.commons.io.IOUtils;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONTokener;

import android.content.res.AssetManager;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.view.WindowManager;
import android.widget.SeekBar;
import android.widget.SeekBar.OnSeekBarChangeListener;
import android.widget.TextView;

import com.google.android.maps.GeoPoint;
import com.google.android.maps.MapActivity;
import com.google.android.maps.MapController;
import com.google.android.maps.MapView;
import com.google.android.maps.Overlay;
import com.google.android.maps.OverlayItem;

public class RomeBattlesActivity extends  MapActivity implements OnSeekBarChangeListener, BattleItemizedOverlayListener
{
	//map items
	MapView mapView;
	MapController mapController;
	BattleItemizedOverlay landBattleOverlay, civilLandBattleOverlay, seaBattleOverlay, civilSeaBattleOverlay;
	ArrayList<Battle> battles;
	
	//Views
	BattleDetailView battleDetailView;
	
	//interact items
	SeekBar		seekBar;
	TextView 	textView;
	
	int maxDate, minDate, battleSpan=10;
		
   /** Called when the activity is first created. */
   @Override
   public void onCreate(Bundle savedInstanceState) {
	   // Hide the Status Bar
	   getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
   	
   	   super.onCreate(savedInstanceState);
       setContentView(R.layout.main);
       
       /*
        * Initialize interface elements
        */        
       initMap();
       initBattleData();
       initSeeker();
       initBattleDetailView();
   }
   
   /*
    * Initialize map
    */
   private void initMap(){
       /*
        * Set up map view 
        */  
	   mapView = (MapView)findViewById(R.id.mapView);
       mapView.displayZoomControls(false);
       mapView.setSatellite(true);

       //set map initial view centered on rome
       int romeLat = (int) (41.9*1E6);
       int romeLon = (int) (12.5*1E6);
       mapController = mapView.getController();
       mapController.setCenter(new GeoPoint(romeLat, romeLon));
       mapController.setZoom(5);
   }
   
   /*
    * grab battle data and start storing
    */
   private void initBattleData(){
   		//pull battle data
       	battles = new ArrayList<Battle>();
       	AssetManager assMgr = getAssets();
       	String battle_json = "";
       
       	//pull json file
       	try{
       		InputStream isStream = assMgr.open("battles.json");
       		StringWriter writer = new StringWriter();
       		IOUtils.copy(isStream, writer, "UTF-8");
       		battle_json = writer.toString();
       	}catch(IOException e){}
       
       	//read json file
       	JSONTokener tokener 	= new JSONTokener(battle_json);
       	try{
       		JSONObject battles_obj	= (JSONObject)tokener.nextValue();
       		JSONArray battles_arr	= battles_obj.getJSONArray("battles");
       	   	
	       	for(int i=0; i<battles_arr.length(); i++){
	       		JSONObject battle_obj = (JSONObject)battles_arr.get(i);
	       		
	       		Battle newBattle = new Battle();
	       		newBattle.loadBattleData(battle_obj);
	       		battles.add(newBattle);       		
	       	}
       	}catch(JSONException e){}
       
       	minDate = (battles.get(0)).getBattleYear();
       	maxDate = (battles.get(battles.size()-1)).getBattleYear();    	
   	}
   
   /*
    * Initialize the seeker stuff
    */
   	private void initSeeker(){
   	//grab interface items
       seekBar  = (SeekBar)findViewById(R.id.seekBar1);
       seekBar.setOnSeekBarChangeListener(this);
       textView = (TextView)findViewById(R.id.sliderOut_txt);        
       
       seekBar.setMax(maxDate-minDate);
       onProgressChanged(seekBar, 0, false);
       onStopTrackingTouch(seekBar);
   }
   
   	private void initBattleDetailView(){
	   battleDetailView = (BattleDetailView)findViewById(R.id.battleDetailView);
	   battleDetailView.invalidate();
	}
   
   @Override
   protected boolean isRouteDisplayed() {
   	// IMPORTANT: This method must return true if your Activity
   	// is displaying driving directions. Otherwise return false.
   	return false;
   }
   
   /* Seekbar Change Listener Interface
    * 
    * This function updates the date span when the slider is moved
    */    
   public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
   	int currYear = minDate+seekBar.getProgress();
   	
   	int lowerYear	= currYear-battleSpan;
   	String fromYear	= (lowerYear<0)?(Integer.toString(Math.abs(lowerYear))+" BCE"):(Integer.toString(lowerYear)+" CE");
   	int upperYear 	= currYear+battleSpan;
   	String toYear	= (lowerYear<0)?(Integer.toString(Math.abs(upperYear))+" BCE"):(Integer.toString(upperYear)+" CE");
   	
   	textView.setText(fromYear+" - "+toYear);   
   	
   	onStopTrackingTouch(seekBar);//refresh map
   }
   
   /* 
    * On stop tracking listener for seek bar
    * 
    * on stop seek this view will figure out wich battles are suppose to be visible on the map, and
    * and then refresh the map
    * 
    * @param seekBar, the seekbar being tracked 
    * @return void
    */  
   public void onStopTrackingTouch(SeekBar seekBar) {
   	int currYear = minDate+seekBar.getProgress();
   	
       //add battle overlay to map
       List<Overlay> mapOverlays 	= mapView.getOverlays();
       mapOverlays.clear();
       
       /*
        * add battle data to the map
        */
       Drawable drawable 			= this.getResources().getDrawable(R.drawable.land_battle);
       landBattleOverlay			= new BattleItemizedOverlay(drawable);
       landBattleOverlay.delegate	= this;
       
       drawable	 						= this.getResources().getDrawable(R.drawable.land_civil_battle);
       civilLandBattleOverlay			= new BattleItemizedOverlay(drawable);
       civilLandBattleOverlay.delegate	= this;
       
       drawable 					= this.getResources().getDrawable(R.drawable.sea_battle);
       seaBattleOverlay				= new BattleItemizedOverlay(drawable);
       seaBattleOverlay.delegate	= this;
       
       drawable 						= this.getResources().getDrawable(R.drawable.sea_civil_battle);
       civilSeaBattleOverlay			= new BattleItemizedOverlay(drawable);
       civilSeaBattleOverlay.delegate	= this;
       
       for(int i=0; i<battles.size(); i++){
       	
    	   Battle currBattle = battles.get(i);
       
    	   if(Math.abs(currBattle.getBattleYear()-currYear) < battleSpan){
       		
    		   int lat = (int) (currBattle.getLat()*1E6);
               int lon = (int) (currBattle.getLon()*1E6);
           	
           	
               GeoPoint point = new GeoPoint(lat,lon);
               OverlayItem overlayitem = new OverlayItem(point, Integer.toString(i), currBattle.getBattleName());
               
               /*
                * Determine what king of battle it was Naval/Land, civil/foreign?
                */
               if(currBattle.getCivil()){
            	   if(currBattle.getNaval()){
            		   civilSeaBattleOverlay.addOverlay(overlayitem); 
            	   }else{
            		   civilLandBattleOverlay.addOverlay(overlayitem);
            	   }
               }else{
	               	if(currBattle.getNaval()){
	               		seaBattleOverlay.addOverlay(overlayitem);
	               	}else{
	               		landBattleOverlay.addOverlay(overlayitem);
	               	}
               }
           }
       }
       
       /*
        * Adding empty overlays causes errors on map move
        */
       if(landBattleOverlay.size() > 0){
    	   mapOverlays.add(landBattleOverlay);
       }
       if(civilLandBattleOverlay.size() > 0){
    	   mapOverlays.add(civilLandBattleOverlay);
       }
       if(seaBattleOverlay.size() > 0){
    	   mapOverlays.add(seaBattleOverlay);
       }
       if(civilSeaBattleOverlay.size() > 0){
    	   mapOverlays.add(civilSeaBattleOverlay);
       }
       
       mapView.invalidate();
   }
   
   public void onStartTrackingTouch(SeekBar seekBar) {
   	// TODO Auto-generated method stub    	
   }
   
   /*
    * Battle Itemized Overlay Interfact 
    */
   public void battleSelectedAtIndex(int index){
	   Battle selectedBattle = battles.get(index);
	   battleDetailView.showBattle(selectedBattle);
   }
}