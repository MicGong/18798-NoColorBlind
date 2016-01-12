package com.jiangong.nocolorblind.activities;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;

import com.jiangong.nocolorblind.R;

public class IshiTestActivity extends Activity {
    private static final String imageName = "ishihara_plate";

    Button prevButton;
    Button nextButton;
    Button nextTestButton;
    EditText userInput;

    int curr_plate = 0;
    int[] user_result = new int[15];


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ishi_test);

        prevButton = (Button)findViewById(R.id.prevBtn);
        nextButton = (Button)findViewById(R.id.nextBtn);
        userInput = (EditText)findViewById(R.id.userInput);

        nextTestButton = (Button)findViewById(R.id.toAnomBtn);

        nextButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                if (curr_plate <= 15) {
                    ImageView testImage = (ImageView)findViewById(R.id.testImageView);
                    int idTemp = getResources()
                            .getIdentifier(imageName + String.valueOf(++curr_plate),
                                    "drawable", getPackageName());
                    testImage.setImageResource(idTemp);
                    //TODO save result
                }
                // TODO no user input
            }
        });

        prevButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (curr_plate >= 0) {
                    ImageView testImage = (ImageView)findViewById(R.id.testImageView);
                    int idTemp = getResources()
                            .getIdentifier(imageName + String.valueOf(--curr_plate),
                                    "drawable", getPackageName());
                    testImage.setImageResource(idTemp);
                    //TODO save result
                }
                // TODO no user input
            }
        });

        nextTestButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent test = new Intent(IshiTestActivity.this, AnomTestActivity.class);
                //TODO add extra info
                // test.putExtra();
                startActivity(test);
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_ishi_test, menu);
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
}
