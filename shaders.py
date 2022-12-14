vertex_shader = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;
out vec3 outColor;
out vec2 outTexCoords;
void main()
{
    vec4 norm = vec4(normal, 0.0);
    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;
    vec4 light = vec4(pointLight, 1.0);
    float intensity = dot(modelMatrix * norm, normalize(light - pos));
    gl_Position = projectionMatrix * viewMatrix * pos;
    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2) * intensity;
    outTexCoords = texCoords;
}
"""


fragment_shader = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
uniform sampler2D tex;
void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
}
"""


#toon shader basado en shader de modulo 1 del curso
toon_shader = """

uniform vec3 lightDir;
varying vec3 normal;
out vec3 outColor;


void main(){
    float intensity;
    intensity = dot(lightDir, normalize(normal));
    
    if intensity > 0.7
        intensity = 1
    if intensity > 0.3
        intensity = 0.5
    else
        intensity = 0.5
        
    outColor = outColor * intensity
}

"""

shader= """

uniform vec3 lightDir;
varying vec3 normal;

void main(){
    float intensity;
    intensity = dot(lightDir, normalize(normal));
    
    if (intensity > 0.80)
       
        
    if (intensity > 0.40)
        
        
    if (intensity > 0.15)
        
        
    else
        
    
}

"""

