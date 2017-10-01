package edu.purdue.duan35.whats_there;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.squareup.okhttp.Callback;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;

import org.w3c.dom.Text;

import java.io.IOException;
import java.util.ArrayList;

public class Recipe extends AppCompatActivity {
    Button mButton;
    EditText mEdit;
    String mText;
    String[] recipe;
    String[] miss;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recipe);
        Intent intent = getIntent();
        mButton = (Button) findViewById(R.id.button1);
        mButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mEdit = (EditText) findViewById(R.id.editText1);
                //mText = (TextView)findViewById(R.id.textView1);
                mText = mEdit.getText().toString();
                Senddata();
//                new RetrieveText();

            }
        });


    }

    class RetrieveText extends AsyncTask<String, Void, Void> {

        Response response;
        TextView missText;
        RetrieveText(Response response) {
            this.response = response;
            this.onPostExecute(null);
        }

        @Override
        protected void onPostExecute(Void aVoid) {
            final TextView missText = (TextView) findViewById(R.id.miss);
            missText.setText(recipe[0]);
            missText.setEnabled(true);
        }

        @Override
        protected Void doInBackground(String... params) {
            final TextView missText = (TextView) findViewById(R.id.miss);
            if (!response.isSuccessful()) {
                try {
                    throw new IOException("Unexpected code " + response);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            } else {
                try {
                    recipe = response.body().string().split(":");
                } catch (IOException e) {
                    e.printStackTrace();
                }
                miss = recipe[1].split(";");
                //System.out.println("Alp sucks");
                String temp = "";
                for (String str : miss) {
                    temp += str;
                }


            }
            return null;
        }
    }

    
    /*public void receivedata() {
        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder()
                .url("http://c62aead8.ngrok.io/recipe/"+mText)
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
                    recipe = response.body().string().split(":");
                    miss = recipe[1].split(";");
                    System.out.println("Alp sucks");
                   /* for (String str : miss) {
                        finalText.setText(str + "\n");
                    }
                    finalText.setEnabled(true);
                    Intent intent = new Intent(Recipe.this, MainActivity.class);
                    startActivity(intent);*/
               /* }
            }
        });


    }*/


        public void Senddata() {


            final String[] option = new String[1];
            OkHttpClient client = new OkHttpClient();
            Request request = new Request.Builder()
                    .url("http://4403d7c6.ngrok.io/recipe/" + mText)
                    .build();
            client.newCall(request).enqueue(new Callback() {
                @Override
                public void onFailure(Request request, IOException e) {
                    e.printStackTrace();
                }

                @Override
                public void onResponse(Response response) throws IOException {

                    //new RetrieveText(response);
                    //Intent intent = new Intent(Recipe.this, MainActivity.class);
                    //startActivity(intent);
                }


            });


        }

    public void back(View view) {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }



}
