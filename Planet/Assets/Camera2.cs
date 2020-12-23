using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Camera2 : MonoBehaviour
{
    public GameObject obj1;
    public GameObject obj2;
    public GameObject obj3;
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        Vector3 center = (obj1.transform.position + obj2.transform.position + obj3.transform.position)/3;
        float distance = Mathf.Max((obj2.transform.position - obj1.transform.position).magnitude, (obj2.transform.position - obj3.transform.position).magnitude, (obj3.transform.position - obj2.transform.position).magnitude);
        transform.position = new Vector3(center.x, center.y + distance+10, center.z);
    }
}