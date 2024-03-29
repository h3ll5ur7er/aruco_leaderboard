/* 
 * API
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// Events
    /// </summary>
    [DataContract]
    public partial class Events :  IEquatable<Events>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Events" /> class.
        /// </summary>
        /// <param name="events">events.</param>
        public Events(List<Event> events = default(List<Event>))
        {
            this._Events = events;
        }
        
        /// <summary>
        /// Gets or Sets _Events
        /// </summary>
        [DataMember(Name="events", EmitDefaultValue=false)]
        public List<Event> _Events { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class Events {\n");
            sb.Append("  _Events: ").Append(_Events).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as Events);
        }

        /// <summary>
        /// Returns true if Events instances are equal
        /// </summary>
        /// <param name="input">Instance of Events to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(Events input)
        {
            if (input == null)
                return false;

            return 
                (
                    this._Events == input._Events ||
                    this._Events != null &&
                    this._Events.SequenceEqual(input._Events)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this._Events != null)
                    hashCode = hashCode * 59 + this._Events.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
