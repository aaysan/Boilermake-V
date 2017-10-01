package edu.purdue.duan35.whats_there;

import android.content.DialogInterface;
import android.content.Intent;
import android.net.Uri;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;

import com.squareup.okhttp.Call;
import com.squareup.okhttp.Callback;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.net.*;


public class MainActivity extends AppCompatActivity {
    CheckBox checkBox1;
    String[] option = new String[10];
    OkHttpClient client = new OkHttpClient();
    Request request = new Request.Builder()
            .url("http://4403d7c6.ngrok.io/object/")
            .build();


    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        checkBox1 = (CheckBox) findViewById(R.id.checkBox1);

        Button button = (Button)findViewById(R.id.button1);
        Button button2 = (Button) findViewById(R.id.button4);
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, Recipe.class);
                startActivity(intent);
            }
        });
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
//                    option = getHTML("http://google.com").split(";");
//                    new GetUrlContentTask(" ").execute("http://google.com");

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
                            option = response.body().string().split(";");
                            //System.out.println(response.body().string());
                          /*  for (int i = 0; i < 100000; i++) {

                            }*/
//                            System.out.println(tmp);
                            Intent intent = new Intent(MainActivity.this, Add.class);
                            intent.putExtra("check1", option[0]);
                            intent.putExtra("check2", option[1]);
                            intent.putExtra("check3", option[2]);
                            intent.putExtra("check4", option[3]);
                            intent.putExtra("check5", option[4]);
                            intent.putExtra("check6", option[5]);
                            intent.putExtra("check7", option[6]);
                            intent.putExtra("check8", option[7]);
                            intent.putExtra("check9", option[8]);
                            intent.putExtra("check10", option[9]);
                            startActivity(intent);
                        }
                    }
                });
                //;


            }

        });

    }



    public void list (View view) {
        Intent intent = new Intent(this, List.class);
        startActivity(intent);
    }

    public void add (View view) {
        //checkBox1.setText(option[0]);
        Intent intent = new Intent(MainActivity.this, Add.class);
        startActivity(intent);

    }



    /*private void goToUrl (String url) {
        Uri uriUrl = Uri.parse(url);
        Intent launchBrowser = new Intent(Intent.ACTION_VIEW, uriUrl);
        startActivity(launchBrowser);
    }*/

//    class GetUrlContentTask extends AsyncTask<String, Integer, String> {
//        public GetUrlContentTask(String s) {
//        }
//
//        protected String doInBackground(String... urls) {
//            URL url = null;
//            try {
//                url = new URL(urls[0]);
//            } catch (MalformedURLException e) {
//                e.printStackTrace();
//            }
//            HttpURLConnection connection = null;
//            try {
//                connection = (HttpURLConnection) url.openConnection();
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//            try {
//                connection.setRequestMethod("GET");
//            } catch (ProtocolException e) {
//                e.printStackTrace();
//            }
//            connection.setDoOutput(true);
//            connection.setConnectTimeout(5000);
//            connection.setReadTimeout(5000);
//            try {
//                connection.connect();
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//            BufferedReader rd = null;
//            try {
//                rd = new BufferedReader(new InputStreamReader(connection.getInputStream()));
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//            String content = "", line;
//            try {
//                while ((line = rd.readLine()) != null) {
//                    content += line + "\n";
//                }
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//            return content;
//        }
//
//        protected void onProgressUpdate(Integer... progress) {
//        }
//
//        protected void onPostExecute(String result) {
//            // this is executed on the main thread after the process is over
//            // update your UI here
//            Intent intent = new Intent(MainActivity.this, Add.class);
//            startActivity(intent);
//        }
//    }


}

