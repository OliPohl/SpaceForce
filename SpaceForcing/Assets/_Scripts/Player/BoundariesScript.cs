using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BoundariesScript : MonoBehaviour
{
    private Vector2 ScreenBounds;

    private float ObjectWidth;
    private float ObjectHeight;
    

    void Start()
    {
        ScreenBounds = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, Camera.main.transform.position.z));

        ObjectWidth = transform.GetComponent<SpriteRenderer>().bounds.size.x / 2;
        ObjectHeight = transform.GetComponent<SpriteRenderer>().bounds.size.y / 2;
    }

    
    void LateUpdate()
    {
        Vector3 ViewPos = transform.position;
        ViewPos.x = Mathf.Clamp(ViewPos.x, ((ScreenBounds.x + ObjectWidth) * -1), (ScreenBounds.x + ObjectWidth));
        ViewPos.y = Mathf.Clamp(ViewPos.y, ((ScreenBounds.y + ObjectHeight) * -1), (ScreenBounds.y + ObjectHeight));
        transform.position = ViewPos;
    }
}
