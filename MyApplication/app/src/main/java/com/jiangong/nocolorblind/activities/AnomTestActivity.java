package com.jiangong.nocolorblind.activities;

import android.app.Activity;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.SeekBar;
import android.widget.TextView;

import com.jiangong.nocolorblind.R;

public class AnomTestActivity extends Activity {

    private static int MIN_VALUE = 99;
    private static int MAX_VALUE = 255;

    SeekBar seekBar;
    TextView image1;
    TextView image2;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_anom_test);

        seekBar = (SeekBar)findViewById(R.id.seekBar);
        image1 = (TextView)findViewById(R.id.image1);
        image2 = (TextView)findViewById(R.id.image2);

        image1.setBackgroundColor(Color.rgb(146,243,0));

        seekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {

            int prog = 0;
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                prog = progress;
                int tempR = parseSeekbar(prog, seekBar.getMax());
                image2.setBackgroundColor(Color.rgb(tempR, tempR, 0));
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
                int tempR = parseSeekbar(prog, seekBar.getMax());
                image2.setBackgroundColor(Color.rgb(tempR, tempR, 0));
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_anom_test, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    private int parseSeekbar(int progress, int seekBarMax) {
        double portion = (double)progress / (double) seekBarMax;
        int temp = (int)((double)MAX_VALUE * portion);
        return temp;
    }
}
