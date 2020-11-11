using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;


public class Script : MonoBehaviour
{
    public GameObject obj;
    public float L=6;
    public float x_0;
    public float v_0;
    private float g = 9.81f;
    private float omega;
    private float A;
    private float thetta;
    private float t=0f;
    private float zPos;
    
    // Start is called before the first frame update
    void Start()
    {
        omega = Mathf.Sqrt(L / g);
        A = Mathf.Sqrt(x_0 * x_0 + v_0 * v_0 / (omega * omega));
        if (v_0 != 0)
            thetta = Mathf.Atan(x_0 * omega / v_0);
        else
            thetta = Mathf.PI/2;
        zPos = obj.transform.position.z;
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        t += Time.fixedDeltaTime;
        float x = A * Mathf.Sin(thetta + omega * t);
        float xPos = L * Mathf.Sin(x);
        float yPos = -L * Mathf.Cos(x);
        obj.transform.position = new Vector3(xPos, yPos, zPos);
    }
}
