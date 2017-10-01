package edu.purdue.duan35.whats_there;

import android.content.Context;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.view.inputmethod.EditorInfo;
import android.view.inputmethod.InputMethodManager;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.squareup.okhttp.Callback;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;

import java.io.IOException;
import java.util.ArrayList;

public class Add extends AppCompatActivity {

    String selection = "";
    String quantity = "";
    EditText quan;
    TextView finalText;
    CheckBox check1;
    CheckBox check2;
    CheckBox check3;
    CheckBox check4;
    CheckBox check5;
    CheckBox check6;
    CheckBox check7;
    CheckBox check8;
    CheckBox check9;
    CheckBox check10;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add);
        Intent intent = getIntent();
        String chk1Str = intent.getStringExtra("check1");
        String chk2Str = intent.getStringExtra("check2");
        String chk3Str = intent.getStringExtra("check3");
        String chk4Str = intent.getStringExtra("check4");
        String chk5Str = intent.getStringExtra("check5");
        String chk6Str = intent.getStringExtra("check6");
        String chk7Str = intent.getStringExtra("check7");
        String chk8Str = intent.getStringExtra("check8");
        String chk9Str = intent.getStringExtra("check9");
        String chk10Str = intent.getStringExtra("check10");

        finalText = (TextView) findViewById(R.id.final_result);
        check1 = (CheckBox) findViewById(R.id.checkBox1);
        check1.setText(chk1Str);

        check2 = (CheckBox) findViewById(R.id.checkBox2);
        check2.setText(chk2Str);

        check3 = (CheckBox) findViewById(R.id.checkBox3);
        check3.setText(chk3Str);

        check4 = (CheckBox) findViewById(R.id.checkBox4);
        check4.setText(chk4Str);

        check5 = (CheckBox) findViewById(R.id.checkBox5);
        check5.setText(chk5Str);

        check6 = (CheckBox) findViewById(R.id.checkBox6);
        check6.setText(chk6Str);

        check7 = (CheckBox) findViewById(R.id.checkBox7);
        check7.setText(chk7Str);

        check8 = (CheckBox) findViewById(R.id.checkBox8);
        check8.setText(chk8Str);

        check9 = (CheckBox) findViewById(R.id.checkBox9);
        check9.setText(chk9Str);

        check10 = (CheckBox) findViewById(R.id.checkBox10);
        check10.setText(chk10Str);
        finalText.setEnabled(false);


    }

    public void back(View view) {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);

    }

    public void selectItem(View view) {
        boolean checked = ((CheckBox) view).isChecked();
        switch (view.getId()) {
            case R.id.checkBox1:
                if (checked) {
                    this.selection = (String) check1.getText();
                }
                break;
            case R.id.checkBox2:
                if (checked) {
                    selection = (String) check2.getText();
                }
                break;
            case R.id.checkBox3:
                if (checked) {
                    selection = (String) check3.getText();
                }
                break;
            case R.id.checkBox4:
                if (checked) {
                    selection = (String) check4.getText();
                }
                break;
            case R.id.checkBox5:
                if (checked) {
                    selection = (String) check5.getText();
                }
                break;
            case R.id.checkBox6:
                if (checked) {
                    selection = (String) check6.getText();
                }
                break;
            case R.id.checkBox7:
                if (checked) {
                    selection = (String) check7.getText();
                }
                break;
            case R.id.checkBox8:
                if (checked) {
                    selection = (String) check8.getText();
                }
                break;
            case R.id.checkBox9:
                if (checked) {
                    selection = (String) check9.getText();
                }
                break;
            case R.id.checkBox10:
                if (checked) {
                    selection = (String) check10.getText();
                }
                break;
        }




    }

    public void Senddata(){
        final String[] option = new String[1];
        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder()
                .url("http://4403d7c6.ngrok.io/add/"+selection+" "+quantity+" 1")
                .build();
        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Request request, IOException e) {
                e.printStackTrace();
            }

            @Override
            public void onResponse(Response response) throws IOException {
                if (!response.isSuccessful()) {
                    throw new IOException("Unexpected code " + response);
                } else {
                    option[0] = response.body().string();
                }
            }

        });

    }

    public void finalSelection(View view) {
        quan = (EditText)findViewById(R.id.quantity);
        quantity = quan.getText().toString();
        finalText.setText(selection);
        finalText.setEnabled(true);
        Senddata();
        Intent intent = new Intent(Add.this, MainActivity.class);
        startActivity(intent);
    }




}
